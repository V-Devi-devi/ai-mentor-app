from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
print("API Key:", API_KEY)

client = genai.Client(api_key=API_KEY)

models = [
    "gemini-2.5-flash",
    "gemini-2.0-flash",
    "gemini-1.5-flash",
    "gemini-1.5-pro"
]

for model in models:
    try:
        response = client.models.generate_content(
            model=model,
            contents="Say Hello"
        )
        print(f"\n{model} : WORKING")
        print(response.text)

    except Exception as e:
        print(f"\n{model} : FAILED")
        print(e)