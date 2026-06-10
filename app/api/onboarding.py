from fastapi import APIRouter
from app.schemas.onboarding import OnboardingRequest

router = APIRouter()

@router.post("/submit")
def submit_onboarding(data: OnboardingRequest):

    return {
        "message": "Onboarding Completed",
        "data": data
    }