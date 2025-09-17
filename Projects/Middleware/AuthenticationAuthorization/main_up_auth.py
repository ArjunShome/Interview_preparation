# main.py
from datetime import datetime, timedelta, timezone
from typing import Dict, Optional, List

import jwt
from fastapi import Depends, FastAPI, HTTPException, status, Security
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm, SecurityScopes
from passlib.context import CryptContext
from pydantic import BaseModel

# ----------------------------
# Config
# ----------------------------
SECRET_KEY = "change-me-please"           # use a strong secret from env in production
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# ----------------------------
# Users "DB" (demo)
# ----------------------------
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_pw(p: str) -> str:
    return pwd_context.hash(p)

def verify_pw(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)

class UserInDB(BaseModel):
    username: str
    hashed_password: str
    disabled: bool = False
    roles: List[str] = []
    scopes: List[str] = []

# demo users
fake_users: Dict[str, UserInDB] = {
    "alice": UserInDB(
        username="alice",
        hashed_password=hash_pw("wonderland"),
        roles=["user"],
        scopes=["products:read"]
    ),
    "admin": UserInDB(
        username="admin",
        hashed_password=hash_pw("swordfish"),
        roles=["admin"],
        scopes=["products:read", "products:write"]
    ),
}

# ----------------------------
# Token models
# ----------------------------
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    sub: Optional[str] = None
    scopes: List[str] = []
    roles: List[str] = []

class UserPublic(BaseModel):
    username: str
    roles: List[str]
    scopes: List[str]

# ----------------------------
# OAuth2 bearer with scopes
# ----------------------------
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="token",
    scopes={
        "products:read": "Read product data",
        "products:write": "Modify product data",
        "admin": "Administrative access",
    },
)

# ----------------------------
# Auth helpers
# ----------------------------
def authenticate_user(username: str, password: str) -> Optional[UserInDB]:
    user = fake_users.get(username)
    if not user or not verify_pw(password, user.hashed_password) or user.disabled:
        return None
    return user

def create_access_token(*, sub: str, scopes: List[str], roles: List[str], expires_minutes: int) -> str:
    now = datetime.now(timezone.utc)
    payload = {
        "sub": sub,
        "iat": int(now.timestamp()),
        "nbf": int(now.timestamp()),
        "exp": int((now + timedelta(minutes=expires_minutes)).timestamp()),
        "scopes": scopes,
        "roles": roles,
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def decode_token(token: str) -> TokenData:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return TokenData(
            sub=payload.get("sub"),
            scopes=payload.get("scopes", []),
            roles=payload.get("roles", []),
        )
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired", headers={"WWW-Authenticate": "Bearer"})
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token", headers={"WWW-Authenticate": "Bearer"})

# Dependency: get current user and enforce requested scopes
async def get_current_user(security_scopes: SecurityScopes, token: str = Depends(oauth2_scheme)) -> UserInDB:
    token_data = decode_token(token)
    if token_data.sub is None:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")

    user = fake_users.get(token_data.sub)
    if not user or user.disabled:
        raise HTTPException(status_code=401, detail="User disabled or not found")

    # Validate requested scopes (AND semantics)
    requested = set(security_scopes.scopes)
    granted = set(token_data.scopes)
    if requested and not requested.issubset(granted):
        raise HTTPException(
            status_code=403,
            detail=f"Insufficient scope. Required: {requested}, token has: {granted}",
        )
    return user

# Simple role-check dependency
def require_roles(*required_roles: str):
    async def dep(user: UserInDB = Security(get_current_user)):
        if not set(required_roles).issubset(set(user.roles)):
            raise HTTPException(status_code=403, detail="Insufficient role")
        return user
    return dep

# ----------------------------
# FastAPI app & routes
# ----------------------------
app = FastAPI(title="Auth with OAuth2 + JWT (username/password)")

@app.post("/token", response_model=Token, summary="Username/password login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    """
    Expects `application/x-www-form-urlencoded` with fields:
    - username
    - password
    - scope: optional space-separated scopes (e.g., "products:read products:write")
    """
    user = authenticate_user(form.username, form.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    # Optional: restrict granted scopes to those the user actually owns
    requested_scopes = set(form.scopes) if hasattr(form, "scopes") else set()
    allowed_scopes = list(set(user.scopes).intersection(requested_scopes or set(user.scopes)))

    token = create_access_token(
        sub=user.username,
        scopes=allowed_scopes,
        roles=user.roles,
        expires_minutes=ACCESS_TOKEN_EXPIRE_MINUTES,
    )
    return Token(access_token=token, token_type="bearer")

@app.get("/me", response_model=UserPublic, summary="Who am I?")
async def read_me(current: UserInDB = Security(get_current_user)):
    return UserPublic(username=current.username, roles=current.roles, scopes=current.scopes)

@app.get(
    "/products",
    summary="Read products (requires products:read)",
)
async def read_products(current: UserInDB = Security(get_current_user, scopes=["products:read"])):
    return {"items": ["Widget A", "Widget B"], "user": current.username}

@app.post(
    "/products",
    summary="Write products (requires products:write)",
)
async def write_products(current: UserInDB = Security(get_current_user, scopes=["products:write"])):
    return {"status": "created", "by": current.username}

@app.get(
    "/admin/metrics",
    summary="Admin-only endpoint (role check)",
)
async def admin_metrics(_: UserInDB = Depends(require_roles("admin"))):
    return {"uptime": "123h", "errors_last_24h": 0}