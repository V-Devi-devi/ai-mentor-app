from pydantic import BaseModel


class SystemStats(BaseModel):
    total_users: int
    total_tasks: int
    total_roadmaps: int
    total_interviews: int
    total_chats: int