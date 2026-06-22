from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.base import Base


class Interview(Base):
    __tablename__ = "interviews"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    score = Column(Integer)
    feedback = Column(String)