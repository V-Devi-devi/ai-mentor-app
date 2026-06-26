import os
import time

from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(
    api_key=API_KEY
)


def ask_gemini(prompt: str):

    retries = 3

    for _ in range(retries):

        try:

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            return response.text

        except Exception as e:

            error = str(e)

            if "503" in error:
                time.sleep(2)
                continue

            return f"AI Error: {error}"

    return "AI Error: Gemini server busy. Please try again later."