from __future__ import annotations
import os, time, base64, secrets
from typing import Dict, List, Optional, Annotated, Tuple

import jwt
import uvicorn
from fastapi import FastAPI, Request, Depends, HTTPException, status, Body, Query, APIRouter
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel, EmailStr
from starlette.middleware.sessions import SessionMiddleware
from starlette.types import ASGIApp, Receive, Scope, Send
from authlib.integrations.starlette_client import OAuth, OAuthError

"""
ENV you need:

export APP_SECRET="change-me-32-bytes"
export JWT_SECRET="change-me-too"
export BASE_URL="http://127.0.0.1:8000"

# OAuth provider credentials (create apps on each portal)
export OAUTH_GOOGLE_CLIENT_ID="..."
export OAUTH_GOOGLE_CLIENT_SECRET="..."
export OAUTH_GITHUB_CLIENT_ID="..."
export OAUTH_GITHUB_CLIENT_SECRET="..."
export OAUTH_LINKEDIN_CLIENT_ID="..."
export OAUTH_LINKEDIN_CLIENT_SECRET="..."

Run: uvicorn main:app --reload
"""

# -----------------------------
# Config
# -----------------------------
APP_SECRET = os.getenv("APP_SECRET", "dev-secret-change")
JWT_SECRET = os.getenv("JWT_SECRET", "dev-jwt-secret-change")
BASE_URL = os.getenv("BASE_URL", "http://127.0.0.1:8000")

JWT_ISSUER = "your-company"
JWT_AUDIENCE = "your-api"

ACCESS_TTL = 15 * 60           # 15 minutes
REFRESH_TTL = 7 * 24 * 60 * 60 # 7 days

# -----------------------------
# App & OAuth
# -----------------------------
app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=APP_SECRET)

oauth = OAuth()
oauth.register(
    name="google",
    client_id=os.getenv("OAUTH_GOOGLE_CLIENT_ID"),
    client_secret=os.getenv("OAUTH_GOOGLE_CLIENT_SECRET"),
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_kwargs={"scope": "openid email profile"},
)
oauth.register(
    name="github",
    client_id=os.getenv("OAUTH_GITHUB_CLIENT_ID"),
    client_secret=os.getenv("OAUTH_GITHUB_CLIENT_SECRET"),
    authorize_url="https://github.com/login/oauth/authorize",
    access_token_url="https://github.com/login/oauth/access_token",
    api_base_url="https://api.github.com/",
    client_kwargs={"scope": "read:user user:email"},
)
oauth.register(
    name="linkedin",
    client_id=os.getenv("OAUTH_LINKEDIN_CLIENT_ID"),
    client_secret=os.getenv("OAUTH_LINKEDIN_CLIENT_SECRET"),
    authorize_url="https://www.linkedin.com/oauth/v2/authorization",
    access_token_url="https://www.linkedin.com/oauth/v2/accessToken",
    api_base_url="https://api.linkedin.com/v2/",
    client_kwargs={"scope": "r_liteprofile r_emailaddress"},
)

# -----------------------------
# Demo "DB" (in-memory)
# -----------------------------
USERS: Dict[str, Dict] = {
    # Local (username/password) demo user
    "local:alice": {
        "id": "local:alice",
        "username": "alice",
        "password": "wonderland",  # DEMO ONLY — hash in production
        "name": "Alice Liddel",
        "email": "alice@example.com",
        "roles": ["user"],
        "scopes": ["read:profile"],
        "provider": "local",
    },
    # Demo Basic user (middleware-only auth, no token issuance)
    "basic:basicuser": {
        "id": "basic:basicuser",
        "username": "basicuser",
        "password": "basicpass",   # DEMO ONLY
        "name": "Basic User",
        "email": "basic@example.com",
        "roles": ["user"],
        "scopes": ["read:profile"],
        "provider": "basic",
    },
}
DEFAULT_ROLES = ["user"]
DEFAULT_SCOPES = ["read:profile"]

# Passwordless code store: code -> {sub, exp}
MAGIC_CODES: Dict[str, Dict] = {}

# -----------------------------
# Token helpers (access + refresh)
# -----------------------------
def _now() -> int:
    return int(time.time())

def _jti() -> str:
    return secrets.token_urlsafe(24)

def _csrf() -> str:
    return secrets.token_hex(32)

# In production use Redis with TTL for refresh tracking
REFRESH_STORE: Dict[str, Dict] = {}  # jti -> {"sub":..., "revoked": False, "exp": ts}

def issue_access(sub: str, roles: List[str], scopes: List[str]) -> str:
    now = _now()
    payload = {
        "iss": JWT_ISSUER, "aud": JWT_AUDIENCE,
        "iat": now, "nbf": now, "exp": now + ACCESS_TTL,
        "sub": sub, "roles": roles, "scopes": scopes, "typ": "access",
    }
    return jwt.encode(payload, JWT_SECRET, algorithm="HS256")

def issue_refresh(sub: str, csrf_token: str) -> Tuple[str, str]:
    now = _now()
    jti = _jti()
    payload = {
        "iss": JWT_ISSUER, "aud": JWT_AUDIENCE,
        "iat": now, "nbf": now, "exp": now + REFRESH_TTL,
        "sub": sub, "typ": "refresh", "jti": jti, "csrf": csrf_token,
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm="HS256")
    REFRESH_STORE[jti] = {"sub": sub, "revoked": False, "exp": payload["exp"]}
    return token, jti

def decode_jwt(token: str) -> Dict:
    return jwt.decode(
        token, JWT_SECRET, algorithms=["HS256"],
        audience=JWT_AUDIENCE, issuer=JWT_ISSUER
    )

def revoke_refresh(jti: str) -> None:
    if jti in REFRESH_STORE:
        REFRESH_STORE[jti]["revoked"] = True

def is_refresh_valid(jti: str) -> bool:
    row = REFRESH_STORE.get(jti)
    return bool(row and not row["revoked"] and row["exp"] > _now())

# -----------------------------
# Cookie helpers (refresh + CSRF)
# -----------------------------
REFRESH_COOKIE = "refresh_token"
CSRF_COOKIE = "csrf_token"

def set_session_cookies(response: JSONResponse, refresh_jwt: str, csrf_token: str, *, secure: bool = False):
    response.set_cookie(
        key=REFRESH_COOKIE, value=refresh_jwt,
        httponly=True, secure=secure, samesite="lax",
        path="/", max_age=REFRESH_TTL,
    )
    response.set_cookie(
        key=CSRF_COOKIE, value=csrf_token,
        httponly=False, secure=secure, samesite="lax",
        path="/", max_age=REFRESH_TTL,
    )

def clear_session_cookies(response: JSONResponse):
    response.delete_cookie(REFRESH_COOKIE, path="/")
    response.delete_cookie(CSRF_COOKIE, path="/")

# -----------------------------
# AuthN middleware (Bearer access + demo Basic)
# -----------------------------
class AuthMiddleware:
    """
    - Accepts Bearer access JWT (typ=access); attaches claims to request.state.user
    - Accepts Basic (demo) against in-memory USERS (does not mint tokens)
    - Does NOT enforce authorization — use dependencies below
    """
    def __init__(self, app: ASGIApp):
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send):
        if scope["type"] != "http":
            return await self.app(scope, receive, send)

        headers = dict(scope.get("headers") or [])
        authz = headers.get(b"authorization", b"").decode()
        claims = None

        if authz.startswith("Bearer "):
            token = authz.split(" ", 1)[1].strip()
            try:
                payload = decode_jwt(token)
                if payload.get("typ") != "access":
                    raise HTTPException(status_code=401, detail="Wrong token type")
                claims = {
                    "sub": payload["sub"],
                    "roles": payload.get("roles", []),
                    "scopes": payload.get("scopes", []),
                    "provider": payload.get("provider"),
                }
            except Exception:
                claims = None
        elif authz.startswith("Basic "):
            try:
                raw = base64.b64decode(authz.split(" ", 1)[1]).decode()
                username, password = raw.split(":", 1)
            except Exception:
                username, password = "", ""
            user_key = f"basic:{username}"
            u = USERS.get(user_key)
            if u and u.get("password") == password:
                claims = {
                    "sub": u["id"],
                    "roles": u.get("roles", []),
                    "scopes": u.get("scopes", []),
                    "provider": "basic",
                }

        scope.setdefault("state", {})
        scope["state"]["user"] = claims
        return await self.app(scope, receive, send)

app.middleware("http")(AuthMiddleware(app))

# -----------------------------
# Authorization dependencies
# -----------------------------
class User(BaseModel):
    sub: str
    roles: List[str] = []
    scopes: List[str] = []
    provider: Optional[str] = None

def current_user(request: Request) -> Optional[User]:
    c = request.state.user
    if not c:
        return None
    return User(sub=c["sub"], roles=c.get("roles", []), scopes=c.get("scopes", []), provider=c.get("provider"))

def require_auth(user: Annotated[User | None, Depends(current_user)]) -> User:
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication required")
    return user

def require_roles(*required: str):
    def dep(user: Annotated[User, Depends(require_auth)]) -> User:
        if not set(required).issubset(set(user.roles)):
            raise HTTPException(status_code=403, detail="Insufficient role")
        return user
    return dep

def require_scopes(*required: str):
    def dep(user: Annotated[User, Depends(require_auth)]) -> User:
        if not set(required).issubset(set(user.scopes)):
            raise HTTPException(status_code=403, detail="Insufficient scope")
        return user
    return dep

# -----------------------------
# Local username/password login (OAuth2PasswordRequestForm)
# -----------------------------
@app.post("/token")
async def login_with_password(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Standard username/password login:
    - POST x-www-form-urlencoded: username, password
    - Returns access token (JSON) + sets refresh & csrf cookies
    """
    username = form_data.username
    password = form_data.password
    user_key = f"local:{username}"
    u = USERS.get(user_key)
    if not u or u.get("password") != password:
        raise HTTPException(status_code=400, detail="Invalid username or password")

    access = issue_access(sub=u["id"], roles=u["roles"], scopes=u["scopes"])
    csrf_value = _csrf()
    refresh, _ = issue_refresh(sub=u["id"], csrf_token=csrf_value)

    resp = JSONResponse({
        "access_token": access, "token_type": "Bearer", "expires_in": ACCESS_TTL,
        "user": {"id": u["id"], "name": u["name"], "email": u["email"], "roles": u["roles"]},
    })
    set_session_cookies(resp, refresh, csrf_value, secure=False)  # secure=True in prod
    return resp

# -----------------------------
# Passwordless: request + verify (optional)
# -----------------------------
class MagicRequest(BaseModel):
    email: EmailStr

@app.post("/auth/magic/request")
async def magic_request(payload: MagicRequest):
    email = payload.email.lower()
    user_id = f"pwdless:{email}"
    user = USERS.get(user_id)
    if not user:
        user = {
            "id": user_id, "email": email, "name": email.split("@")[0],
            "roles": DEFAULT_ROLES[:], "scopes": DEFAULT_SCOPES[:], "provider": "passwordless",
        }
        USERS[user_id] = user
    code = secrets.token_urlsafe(16)
    MAGIC_CODES[code] = {"sub": user_id, "exp": _now() + 5 * 60}
    # TODO: email link f"{BASE_URL}/auth/magic/verify?code={code}"
    return {"message": "Magic code generated (demo).", "code": code}

@app.get("/auth/magic/verify")
async def magic_verify(code: str = Query(...)):
    data = MAGIC_CODES.get(code)
    if not data or data["exp"] < _now():
        raise HTTPException(status_code=400, detail="Invalid or expired code")
    sub = data["sub"]
    user = USERS.get(sub)
    MAGIC_CODES.pop(code, None)

    access = issue_access(sub=user["id"], roles=user["roles"], scopes=user["scopes"])
    csrf_value = _csrf()
    refresh, _ = issue_refresh(sub=user["id"], csrf_token=csrf_value)

    resp = JSONResponse({
        "access_token": access, "token_type": "Bearer", "expires_in": ACCESS_TTL,
        "user": {"id": user["id"], "name": user["name"], "email": user["email"], "roles": user["roles"]},
    })
    set_session_cookies(resp, refresh, csrf_value, secure=False)
    return resp

# -----------------------------
# Social login (OAuth2)
# -----------------------------
@app.get("/login/{provider}")
async def oauth_login(request: Request, provider: str):
    if provider not in ("google", "github", "linkedin"):
        raise HTTPException(status_code=404, detail="Unknown provider")
    redirect_uri = f"{BASE_URL}/auth/{provider}/callback"
    client = oauth.create_client(provider)
    return await client.authorize_redirect(request, redirect_uri)

@app.get("/auth/{provider}/callback")
async def oauth_callback(request: Request, provider: str):
    if provider not in ("google", "github", "linkedin"):
        raise HTTPException(status_code=404, detail="Unknown provider")
    client = oauth.create_client(provider)
    try:
        _ = await client.authorize_access_token(request)
    except OAuthError as e:
        raise HTTPException(status_code=400, detail=f"OAuth error: {e.error}")

    if provider == "google":
        data = (await client.get("userinfo")).json()
        external_id = f"google:{data['sub']}"
        email = data.get("email")
        name = data.get("name") or data.get("given_name")
    elif provider == "github":
        user = (await client.get("user")).json()
        emails = (await client.get("user/emails")).json()
        primary = next((e["email"] for e in emails if e.get("primary")), None)
        external_id = f"github:{user['id']}"
        email = primary or (emails[0]["email"] if emails else None)
        name = user.get("name") or user.get("login")
    else:  # linkedin
        me = (await client.get("me", params={"projection": "(id,localizedFirstName,localizedLastName)"})).json()
        email_resp = await client.get("emailAddress", params={"q": "members", "projection": "(elements*(handle~))"})
        email_json = email_resp.json()
        email = None
        try:
            email = email_json["elements"][0]["handle~"]["emailAddress"]
        except Exception:
            pass
        external_id = f"linkedin:{me['id']}"
        name = f"{me.get('localizedFirstName','')} {me.get('localizedLastName','')}".strip()

    u = USERS.get(external_id)
    if not u:
        u = {
            "id": external_id, "email": email, "name": name,
            "roles": DEFAULT_ROLES[:], "scopes": DEFAULT_SCOPES[:], "provider": provider,
        }
        USERS[external_id] = u

    access = issue_access(sub=u["id"], roles=u["roles"], scopes=u["scopes"])
    csrf_value = _csrf()
    refresh, _ = issue_refresh(sub=u["id"], csrf_token=csrf_value)

    resp = JSONResponse({
        "access_token": access, "token_type": "Bearer", "expires_in": ACCESS_TTL,
        "user": {"id": u["id"], "name": u["name"], "email": u["email"], "roles": u["roles"]},
    })
    set_session_cookies(resp, refresh, csrf_value, secure=False)
    return resp

# -----------------------------
# Refresh & Logout (CSRF double-submit, rotation)
# -----------------------------
router = APIRouter()

@router.post("/auth/refresh")
async def refresh(request: Request):
    refresh_cookie = request.cookies.get(REFRESH_COOKIE)
    csrf_cookie = request.cookies.get(CSRF_COOKIE)
    csrf_header = request.headers.get("X-CSRF-Token")

    if not refresh_cookie or not csrf_cookie or not csrf_header:
        raise HTTPException(status_code=401, detail="Missing session or CSRF token")

    try:
        payload = decode_jwt(refresh_cookie)
    except Exception as e:
        raise HTTPException(status_code=401, detail=f"Invalid refresh token: {e}")

    if payload.get("typ") != "refresh":
        raise HTTPException(status_code=401, detail="Wrong token type")

    jti = payload.get("jti")
    if not jti or not is_refresh_valid(jti):
        raise HTTPException(status_code=401, detail="Refresh token expired or revoked")

    if not (csrf_header == csrf_cookie == payload.get("csrf")):
        raise HTTPException(status_code=401, detail="CSRF validation failed")

    # Rotate
    revoke_refresh(jti)
    sub = payload["sub"]
    roles = USERS.get(sub, {}).get("roles", DEFAULT_ROLES)
    scopes = USERS.get(sub, {}).get("scopes", DEFAULT_SCOPES)

    new_access = issue_access(sub=sub, roles=roles, scopes=scopes)
    new_refresh, _ = issue_refresh(sub=sub, csrf_token=payload["csrf"])

    resp = JSONResponse({"access_token": new_access, "token_type": "Bearer", "expires_in": ACCESS_TTL})
    set_session_cookies(resp, new_refresh, payload["csrf"], secure=False)
    return resp

@router.post("/auth/logout")
async def logout(request: Request):
    refresh_cookie = request.cookies.get(REFRESH_COOKIE)
    if refresh_cookie:
        try:
            payload = decode_jwt(refresh_cookie)
            jti = payload.get("jti")
            if jti:
                revoke_refresh(jti)
        except Exception:
            pass
    resp = JSONResponse({"ok": True})
    clear_session_cookies(resp)
    return resp

app.include_router(router)

# -----------------------------
# Example routes
# -----------------------------
@app.get("/public")
async def public():
    return {"ok": True, "msg": "Anyone can see this"}

@app.get("/me")
async def me(user: Annotated[User, Depends(require_auth)]):
    return {"sub": user.sub, "roles": user.roles, "scopes": user.scopes, "provider": user.provider}

@app.get("/admin")
async def admin_only(_: Annotated[User, Depends(require_roles("admin"))]):
    return {"ok": True, "msg": "Admins only"}

@app.get("/profile:read")
async def profile_read(_: Annotated[User, Depends(require_scopes("read:profile"))]):
    return {"ok": True, "msg": "Scope read:profile granted"}

@app.get("/healthz")
async def healthz():
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8005, reload=True)