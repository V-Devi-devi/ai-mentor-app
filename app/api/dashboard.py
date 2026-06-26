from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.services.dashboard_service import get_dashboard
from app.core.dependencies import get_current_user
from app.models.user import User

router = APIRouter()


@router.get("/")
def dashboard(
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):

    return get_dashboard(
        db,
        user.id
    )