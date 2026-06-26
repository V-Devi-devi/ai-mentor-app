import time

from app.ai.gemini_client import ask_gemini
from app.ai.memory import save_chat


def generate_response(question):

    retries = 3

    for attempt in range(retries):

        try:
            answer = ask_gemini(question)

            try:
                save_chat(
                    question,
                    answer
                )

            except Exception as e:
                print(
                    "Chat Memory Error:",
                    str(e)
                )

            return answer

        except Exception as e:

            error = str(e)

            print(
                "Gemini Error:",
                error
            )

            # Retry for temporary Gemini errors
            if (
                "503" in error
                or "UNAVAILABLE" in error
                or "429" in error
                or "RESOURCE_EXHAUSTED" in error
            ):

                if attempt < retries - 1:

                    print(
                        f"Retry {attempt + 1}"
                    )

                    time.sleep(2)
                    continue

                return (
                    "AI service is currently busy. "
                    "Please try again after a few minutes."
                )

            return (
                "Unable to generate response: "
                + error
            )