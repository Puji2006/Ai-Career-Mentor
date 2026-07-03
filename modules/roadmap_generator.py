import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")


def generate_roadmap(resume_text):

    prompt = f"""
You are an AI Career Mentor.

Based on this resume create a complete learning roadmap.

Resume:

{resume_text}

Include:

1. Current Skill Level
2. Missing Skills
3. Week-wise Learning Plan (12 Weeks)
4. Best Resources
5. Certifications
6. Projects to Build
7. Interview Preparation Plan
8. Final Career Advice

Return in Markdown.
"""

    response = model.generate_content(prompt)

    return response.text