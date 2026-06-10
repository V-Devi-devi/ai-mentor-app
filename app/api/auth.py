from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials

from app.schemas.auth import (
    RegisterRequest,
    LoginRequest
)

from app.core.auth import create_access_token
from app.core.dependencies import security
from app.core.security import (
    hash_password,
    verify_password
)

router = APIRouter()

# Temporary storage (later replace with PostgreSQL)
users = []


@router.post("/register")
def register(data: RegisterRequest):

    for user in users:
        if user["username"] == data.username:
            raise HTTPException(
                status_code=400,
                detail="Username already exists"
            )

    users.append(
        {
            "username": data.username,
            "password": hash_password(data.password)
        }
    )

    return {
        "message": "User registered successfully"
    }


@router.post("/login")
def login(data: LoginRequest):

    for user in users:

        if user["username"] == data.username:

            if verify_password(
                data.password,
                user["password"]
            ):

                token = create_access_token(
                    {
                        "sub": data.username
                    }
                )

                return {
                    "access_token": token,
                    "token_type": "Bearer",
                    "expires_in": "1 Hour"
                }

    raise HTTPException(
        status_code=401,
        detail="Invalid username or password"
    )


@router.get("/profile")
def profile(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):

    token = credentials.credentials

    return {
        "message": "Authenticated User",
        "token": token
    }