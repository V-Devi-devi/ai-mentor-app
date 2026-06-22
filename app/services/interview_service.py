from app.ai.gemini_client import ask_gemini
from app.ai.prompts import INTERVIEW_PROMPT


def generate_questions(
    role,
    difficulty
):
    prompt = INTERVIEW_PROMPT.format(
        role=role,
        difficulty=difficulty
    )

    return ask_gemini(prompt)