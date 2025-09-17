import datetime
from datetime import timedelta

from fastapi import FastAPI, status, Depends, HTTPException, Security
from fastapi.responses import JSONResponse
from typing_extensions import Optional

from log import logger
import products as pr
import asyncio
import uvicorn
import jwt

from pydantic import BaseModel
from passlib.context import CryptContext
from typing import Dict
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm, SecurityScopes


# ------------------------
# CONFIG
# ------------------------
APP_SECRET_KEY = "356846165587f25eb2a383bf0b8d65553a1b4898591037a80756369cca494497"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRY_MIN = 30


# ------------------------
# USER DB
# ------------------------
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# hash the password
def create_hash(pwd: str):
    hash_value = pwd_context.hash(pwd)
    return hash_value

# verify the password
def verify_pwd(password, password_hash):
    return pwd_context.verify(password, password_hash)

# User Model in Database
class User(BaseModel):
    user_name: str
    user_password: str
    active: bool
    roles: list[str] = []
    scope: list[str] = []

# User Data
fake_user_db_data: Dict[str, User] = {
    "Arjun": User(
        user_name="Arjun",
        user_password=create_hash("Aspwd@202508"),
        active=True,
        roles=["admin"],
        scope=["admin", "user:free", "user:premium"]
    ),
    "Sanchita": User(
        user_name="Sanchita",
        user_password=create_hash("Sanchipwd@202508"),
        active=True,
        roles=["user"],
        scope=["user:premium", "user:free"]
    ),
    "Laltu": User(
        user_name="Laltu",
        user_password=create_hash("Laltupwd@202508"),
        active=True,
        roles=["user"],
        scope=["user:free"]
    ),
}


# ------------------------
# MODELS
# ------------------------

class Product(BaseModel):
    product_name: str
    product_type: str
    product_subscription: str


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenDetails(BaseModel):
    sub: str = None
    scopes: list[str]
    roles: list[str]

class UserAccess(BaseModel):
    username: str
    roles: list[str]
    scope: list[str]

# ------------------------
# OAUTH SETUP
# ------------------------
auth = OAuth2PasswordBearer(
    tokenUrl="token",
    scopes={
        "user:free": "Free Subscription User",
        "user:premium": "Premium Subscription User",
        "admin": "Administrative Access",
    },
)

# helper functions

# Create Access Token
def create_access_token(sub: str, roles: list[str], scopes: list[str], expire_mins: int) -> str:
    now = datetime.datetime.now()
    payload = {
        "sub": sub,
        "iat": int(now.timestamp()),
        "nbf": int(now.timestamp()),
        "exp": int((now + timedelta(minutes=expire_mins)).timestamp()),
        "scopes": scopes,
        "roles": roles
    }
    return jwt.encode(payload, APP_SECRET_KEY, algorithm=ALGORITHM)

# Decode Access Token
def decode_token(token: str) -> TokenDetails:
    try:
        payload = jwt.decode(token, APP_SECRET_KEY, algorithms=[ALGORITHM])
        token_details = TokenDetails(
            sub=payload.get("sub"),
            scopes=payload.get("scopes"),
            roles=payload.get("roles"),
        )
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User Token Expired",
            headers={"WWW-Authenticate": "Bearer"}
        )
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Token",
            headers={"WWW-Authenticate": "Bearer"}
        )
    return token_details

# Authenticate User
def authenticate_user(username: str, password: str) -> Optional[User]:
    user = fake_user_db_data.get(username)
    if user and user.active and verify_pwd(password, user.user_password):
        return user
    return None

# Get current user
def get_current_user(security_scopes: SecurityScopes, token: str = Depends(auth)) -> User:
    token_data = decode_token(token)

    if not token_data.sub:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token Data"
        )
    user = fake_user_db_data.get(token_data.sub)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User Does not Exist"
        )
    if not user.active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User has been deactivated"
        )

    requested = set(security_scopes.scopes)
    granted = set(token_data.scopes)

    if requested and not requested.issubset(granted):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"Insufficient Scope. Required: {requested} but token has {granted}"
        )
    return user

# Required Roles
def require_roles(*required_roles: str):
    async def dep(user: User = Security(get_current_user)):
        if not set(required_roles).issubset(set(user.roles)):
            raise HTTPException(status_code=403, detail="Insufficient role")
        return user
    return dep

# ------------------------
# FastAPI app and routes
# ------------------------

app = FastAPI()

# Login API
@app.post("/token",
          response_model=Token)
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form.username, form.password)
    if not user:
        logger.error("Invalid Username and Password")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid Username and Password"
        )
    requested_scope = set(form.scopes) if hasattr(form, "scopes") else set()
    granted_scope = list(set(user.scope).intersection(requested_scope or set(user.scope)))

    token = create_access_token(
        sub=user.user_name,
        scopes=granted_scope,
        roles=user.roles,
        expire_mins=ACCESS_TOKEN_EXPIRY_MIN,
    )
    return Token(access_token=token, token_type="bearer")


@app.get("/api/v1/get_product_details/{product_id}",
         response_model=Product,
         status_code=status.HTTP_200_OK)
async def get_product_details(product_id: int, current_usr: User=Security(get_current_user, scopes=["user:free"])):
    logger.info("Fetching product details...")
    await asyncio.sleep(0.5)
    result = pr.PRODUCTS.get(product_id, None)
    if result is None:
        logger.error(f"User passed in wrong product ID {product_id}")
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"message": "Product ID requested does not exist, please recheck."}
        )
    logger.info("Product fetched successfully.")
    return result


@app.get("/api/v1/check_products_access",
         response_model=list[Product])
async def check_products_access(user: User=Security(get_current_user, scopes=["user:premium"])):
    # Only authentic customers can access this URL
    # Customers having premium memberships can only have access to all the products,
    # else only free product access to be granted
    products = pr.PRODUCTS.values()
    return products


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8005, reload=True)