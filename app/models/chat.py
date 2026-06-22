from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.base import Base


class Chat(Base):
    __tablename__ = "chats"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    question = Column(String)
    answer = Column(String)