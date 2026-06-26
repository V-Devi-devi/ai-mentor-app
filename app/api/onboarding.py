from fastapi import APIRouter, Depends
from app.schemas.onboarding import OnboardingRequest
from app.core.dependencies import get_current_user
from app.models.user import User

router = APIRouter()

@router.post("/submit")
def submit_onboarding(
    data: OnboardingRequest,
    current_user: User = Depends(get_current_user)
):

    return {
        "message": "Onboarding Completed",
        "user": {
            "id": current_user.id,
            "username": current_user.username,
            "role": current_user.role
        },
        "data": data
    }