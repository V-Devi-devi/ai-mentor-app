from app.ai.gemini_client import ask_gemini


def stream_response(prompt):
    return ask_gemini(prompt)