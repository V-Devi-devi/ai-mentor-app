from pydantic import BaseModel
from typing import List


class RoadmapRequest(BaseModel):
    target_role: str
    current_skills: List[str]
    experience_level: str