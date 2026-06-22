from sqlalchemy import Column, Integer, ForeignKey
from app.db.base import Base


class Analytics(Base):
    __tablename__ = "analytics"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    roadmap_progress = Column(Integer)
    task_progress = Column(Integer)
    interview_score = Column(Integer)