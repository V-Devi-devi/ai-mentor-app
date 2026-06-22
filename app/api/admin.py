from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.services.admin_service import (
    get_system_stats,
    get_all_users,
    delete_user
)
from app.core.dependencies import (
    get_current_user
)

router = APIRouter()


@router.get("/stats")
def stats(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return get_system_stats(db)


@router.get("/users")
def users(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return get_all_users(db)


@router.delete("/users/{user_id}")
def remove_user(
    user_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
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
        "message":
            "User deleted successfully"
    }