from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.auth import (
    RegisterRequest,
    LoginRequest
)

from app.core.auth import create_access_token
from app.core.dependencies import get_current_user
from app.core.security import (
    hash_password,
    verify_password
)

from app.db.session import get_db
from app.models.user import User

router = APIRouter()


# ==========================
# Register
# ==========================
@router.post("/register")
def register(
    data: RegisterRequest,
    db: Session = Depends(get_db)
):

    existing_user = (
        db.query(User)
        .filter(
            User.username == data.username
        )
        .first()
    )

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists"
        )

    new_user = User(
        username=data.username,
        password=hash_password(
            data.password
        ),
        role="user"
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User registered successfully"
    }


# ==========================
# Login
# ==========================
@router.post("/login")
def login(
    data: LoginRequest,
    db: Session = Depends(get_db)
):

    user = (
        db.query(User)
        .filter(
            User.username == data.username
        )
        .first()
    )

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )

    if not verify_password(
        data.password,
        user.password
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )

    token = create_access_token(
        {
            "sub": str(user.id)
        }
    )

    return {
        "access_token": token,
        "token_type": "Bearer"
    }


# ==========================
# Profile
# ==========================
@router.get("/profile")
def profile(
    current_user: User = Depends(
        get_current_user
    )
):

    role = (
        "admin"
        if current_user.role == "admin"
        else "user"
    )

    return {
        "id": current_user.id,
        "username": current_user.username,
        "role": role
    }