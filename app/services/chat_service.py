def generate_response(message: str):

    responses = {
        "python": "Python is a programming language.",
        "sql": "SQL is used to manage databases.",
        "fastapi": "FastAPI is a Python web framework."
    }

    message = message.lower()

    for key in responses:
        if key in message:
            return responses[key]

    return "I am your AI Mentor. Please ask a technical question."