from fastapi import APIRouter, Depends
from app.schemas.onboarding import OnboardingRequest
from app.core.dependencies import get_current_user

router = APIRouter()

@router.post("/submit")
def submit_onboarding(
    data: OnboardingRequest,
    current_user: str = Depends(get_current_user)
):

    return {
        "message": "Onboarding Completed",
        "user": current_user,
        "data": data
    }