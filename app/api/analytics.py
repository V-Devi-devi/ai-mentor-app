from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db

from app.services.analytics_service import (
    get_analytics
)

from app.core.role_checker import (
    role_required
)

from app.models.user import User

router = APIRouter()


@router.get("/")
def analytics(
    db: Session = Depends(get_db),
    current_user: User = Depends(
        role_required(
            ["user", "admin"]
        )
    )
):

    return get_analytics(
        db,
        current_user.id
    )