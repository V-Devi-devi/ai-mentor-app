from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.services.analytics_service import (
    get_analytics
)
from app.core.dependencies import (
    get_current_user
)

router = APIRouter()


@router.get("/")
def analytics(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):

    user_id = user["id"]

    return get_analytics(
        db,
        user_id
    )