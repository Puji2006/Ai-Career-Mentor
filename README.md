# 🎯 AI Career Mentor

An AI-powered career preparation platform that helps students and job seekers analyze resumes, check ATS compatibility, match against job descriptions, and practice interviews with real-time AI feedback — built with Python, Streamlit, and Google Gemini.

---

## 📌 Overview

AI Career Mentor consolidates the fragmented process of resume review, ATS optimization, job matching, and interview preparation into a single AI-assisted platform. It combines rule-based NLP (regex-based parsing) with Google's Gemini large language model to deliver structured, actionable feedback at every stage of job preparation.

---

## ✨ Features

- 📄 **Resume Upload & Parsing** — Extracts name, email, phone, and skills from PDF resumes
- 📊 **ATS Score Checker** — Scores resume compatibility (0–100) with matched/missing skills and improvement tips
- 💼 **Job Description Matcher** — Compares your resume against any job posting and returns a match percentage
- 🧠 **AI Interview Question Generator** — Generates HR, technical, project-based, ML, and coding questions tailored to your resume
- 🎤 **Interactive Interview Practice** — Pick a skill, answer one AI-generated question at a time, and get instant scoring (0–10), strengths, improvement areas, and a model answer
- 📅 **Personalized Learning Roadmap** — Month-by-month upskilling plan with resources, projects, and certifications
- 🤖 **AI Career Chatbot** — Ask open-ended career questions with resume-aware context

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3 |
| Web Framework | Streamlit |
| Generative AI | Google Gemini API (`google-genai`, `gemini-2.5-flash`) |
| PDF Processing | pypdf |
| Data Handling | pandas, NumPy |
| Config Management | python-dotenv |

---

## 📂 Project Structure

```
AI-Career-Mentor/
│
├── app.py                      # Main Streamlit app (UI + navigation)
├── requirements.txt            # Python dependencies
├── .env                        # API keys (not committed)
│
└── modules/
    ├── resume_reader.py         # PDF text extraction
    ├── resume_parser.py         # Extracts name, email, phone, skills
    ├── ats_checker.py           # ATS scoring logic
    ├── job_matcher.py           # Resume vs job description matching
    ├── interview_generator.py   # Bulk interview question generation
    ├── mock_interview.py        # Interactive one-at-a-time interview practice
    ├── roadmap_generator.py     # Personalized learning roadmap
    ├── chatbot.py                # AI career chatbot
    └── gemini_utils.py           # Shared retry-with-backoff for Gemini API calls
```

---

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/AI-Career-Mentor.git
   cd AI-Career-Mentor
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate      # Mac/Linux
   venv\Scripts\activate         # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**

   Create a `.env` file in the project root:
   ```
   GEMINI_API_KEY=your_gemini_api_key_here
   ```
   Get a free API key from [Google AI Studio](https://aistudio.google.com/).

5. **Run the app**
   ```bash
   streamlit run app.py
   ```
   The app will open at `http://localhost:8501`.

---

## 🚀 Usage

1. Go to **📄 Resume Upload** and upload your resume (PDF).
2. Check **📊 ATS Score** to see your compatibility score and missing skills.
3. Paste a job posting under **💼 Job Match** to see how well you fit that specific role.
4. Use **🧠 Interview Generator** for a full question bank, or **🎤 Interview Practice** for interactive, one-question-at-a-time practice with AI feedback.
5. Visit **📅 Learning Roadmap** for a personalized upskilling plan.
6. Ask anything career-related in **🤖 AI Chatbot**.

---

## 🐛 Notable Engineering Decisions

- **Word-boundary skill matching:** Skill detection originally used plain substring search, which caused false positives (e.g., `"C"` matching inside `"Machine"`). Fixed using regex word-boundary (`\b`) matching for accurate whole-word detection.
- **Retry-resilient AI calls:** All Gemini API calls go through a shared `gemini_utils.py` utility implementing exponential backoff, so transient `503 UNAVAILABLE` errors from Google's servers are retried automatically instead of crashing the app.
- **Structured AI output:** The interview practice evaluator prompts Gemini to return strict JSON, enabling reliable parsing into UI elements (score bars, feedback cards) instead of unpredictable free-form text.

---

## 🔮 Future Enhancements

- [ ] Embedding-based semantic skill extraction (beyond fixed keyword lists)
- [ ] Persistent storage (database) for tracking user progress over time
- [ ] Support for DOCX resumes
- [ ] Downloadable PDF/Word export for ATS reports and interview feedback
- [ ] Public deployment with multi-user authentication

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙋 Author

**[Your Name]**
[LinkedIn](#) • [GitHub](#) • [Portfolio](#)
