from pydantic import BaseModel
from typing import List

class OnboardingRequest(BaseModel):
    full_name: str
    college: str
    degree: str
    branch: str
    year: int
    cgpa: float
    skills: List[str]
    target_role: str