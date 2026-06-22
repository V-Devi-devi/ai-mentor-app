from pydantic import BaseModel


class InterviewRequest(BaseModel):
    role: str
    difficulty: str


class AnswerRequest(BaseModel):
    question: str
    answer: str