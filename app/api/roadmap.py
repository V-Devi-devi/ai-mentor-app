from fastapi import APIRouter, Depends

from app.schemas.roadmap import RoadmapRequest
from app.services.roadmap_service import generate_roadmap
from app.core.role_checker import role_required

router = APIRouter()


@router.post("/generate")
def roadmap(
    data: RoadmapRequest,
    user=Depends(
        role_required(
            ["student", "mentor", "admin"]
        )
    )
):

    roadmap = generate_roadmap(
        data.target_role,
        data.current_skills,
        data.experience_level
    )

    return {
        "username": user["username"],
        "role": user["role"],
        "target_role": data.target_role,
        "experience_level": data.experience_level,
        "current_skills": data.current_skills,
        "roadmap": roadmap
    }