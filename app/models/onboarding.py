from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    ForeignKey
)
from app.db.base import Base


class Onboarding(Base):
    __tablename__ = "onboarding"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    full_name = Column(String)
    college = Column(String)
    degree = Column(String)
    branch = Column(String)
    year = Column(Integer)
    cgpa = Column(Float)
    skills = Column(String)
    target_role = Column(String)