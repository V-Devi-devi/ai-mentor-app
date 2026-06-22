from pydantic import BaseModel


class AnalyticsResponse(BaseModel):
    total_tasks: int
    completed_tasks: int
    task_completion_percentage: float

    total_roadmaps: int
    completed_roadmaps: int
    roadmap_completion_percentage: float

    average_interview_score: float
    total_chats: int