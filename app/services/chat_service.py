from app.ai.gemini_client import ask_gemini
from app.ai.memory import save_chat


def generate_response(question):

    answer = ask_gemini(question)

    save_chat(
        question,
        answer
    )

    return answer