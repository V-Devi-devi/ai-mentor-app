from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db

from app.services.admin_service import (
    get_system_stats,
    get_all_users,
    delete_user
)

from app.core.role_checker import role_required
from app.models.user import User
from app.schemas.user import UserResponse

router = APIRouter()


# ==========================
# Admin Stats
# ==========================
@router.get("/stats")
def stats(
    db: Session = Depends(get_db),
    current_user: User = Depends(
        role_required(["admin"])
    )
):
    return get_system_stats(db)


# ==========================
# Get All Users
# ==========================
@router.get("/users", response_model=list[UserResponse])
def users(
    db: Session = Depends(get_db),
    current_user: User = Depends(
        role_required(["admin"])
    )
):
    return get_all_users(db)


# ==========================
# Delete User
# ==========================
@router.delete("/users/{user_id}")
def remove_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        role_required(["admin"])
    )
):

    deleted_user = delete_user(
        db,
        user_id
    )

    if not deleted_user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "message": "User deleted successfully"
    }