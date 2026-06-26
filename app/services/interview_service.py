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

    result = ask_gemini(prompt)

    if isinstance(result, str) and result.startswith("AI Error"):

        return [
            f"What is {role}?",
            f"Explain OOP concepts.",
            f"What are the advantages of Python?",
            f"What is API?",
            f"Explain database normalization."
        ]

    return result


def evaluate_answer(
    question,
    answer
):

    evaluation_prompt = f"""
Question:
{question}

Candidate Answer:
{answer}

Evaluate the answer.

Return:
Score out of 10
Feedback
"""

    result = ask_gemini(
        evaluation_prompt
    )

    if isinstance(result, str) and result.startswith("AI Error"):

        return {
            "score": 5,
            "feedback":
                "AI evaluation unavailable. Manual review required."
        }

    return {
        "score": 8,
        "feedback": result
    }