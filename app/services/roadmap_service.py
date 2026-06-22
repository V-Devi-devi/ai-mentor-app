from app.ai.gemini_client import ask_gemini
from app.ai.prompts import ROADMAP_PROMPT


def generate_roadmap(
    role,
    skills,
    experience_level
):
    prompt = ROADMAP_PROMPT.format(
        role=role,
        skills=skills,
        experience_level=experience_level
    )

    return ask_gemini(prompt)