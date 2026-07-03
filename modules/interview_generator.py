import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")


def generate_interview_questions(resume_text):

    prompt = f"""
You are an experienced Technical Interviewer.

Based on the following resume generate:

1. 10 HR Interview Questions with Answers
2. 10 Technical Interview Questions with Answers
3. 5 Project-based Questions with Answers
4. 5 Machine Learning Questions with Answers
5. 5 Coding Questions (Python/Java) with Answers

Resume:

{resume_text}

Return the response in Markdown format.
"""

    response = model.generate_content(prompt)

    return response.text