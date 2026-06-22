from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.base import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    title = Column(String)
    description = Column(String)
    status = Column(String, default="pending")