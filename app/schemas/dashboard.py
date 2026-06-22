from pydantic import BaseModel


class DashboardResponse(BaseModel):
    username: str
    total_tasks: int
    completed_tasks: int
    task_progress: float

    total_roadmaps: int
    completed_roadmaps: int
    roadmap_progress: float

    average_interview_score: float
    total_chats: int

    overall_performance: float
    recommendation: str