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

    result = ask_gemini(prompt)

    # Fallback roadmap if Gemini fails
    if isinstance(result, str) and result.startswith("AI Error"):

        return f"""
ROADMAP FOR {role.upper()}

WEEK 1
- Learn fundamentals
- Understand core concepts
- Practice beginner problems

WEEK 2
- Learn frameworks and tools
- Build mini project
- Improve coding skills

WEEK 3
- Study advanced topics
- Build real-world project
- Debug and optimize code

WEEK 4
- Mock interviews
- Resume preparation
- Portfolio improvement

Current Skills:
{skills}

Experience Level:
{experience_level}
"""

    return result