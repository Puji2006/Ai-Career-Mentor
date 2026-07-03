import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")


def chat_with_ai(resume_text, question):

    prompt = f"""
You are an AI Career Mentor.

Candidate Resume:

{resume_text}

Candidate Question:

{question}

Give a helpful, detailed answer.
"""

    response = model.generate_content(prompt)

    return response.text