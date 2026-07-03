import streamlit as st

from modules.resume_reader import read_resume
from modules.resume_parser import parse_resume
from modules.ats_checker import calculate_ats
from modules.job_matcher import job_match
from modules.interview_generator import generate_interview_questions
from modules.roadmap_generator import generate_roadmap
from modules.chatbot import chat_with_ai

# ---------------------------------------------------
# Page Config
# ---------------------------------------------------

st.set_page_config(
    page_title="AI Career Mentor",
    page_icon="🎯",
    layout="wide"
)

# ---------------------------------------------------
# Session State
# ---------------------------------------------------

if "resume_text" not in st.session_state:
    st.session_state.resume_text = ""

if "resume_data" not in st.session_state:
    st.session_state.resume_data = {}

# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------

st.sidebar.title("🎯 AI Career Mentor")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "📄 Resume Upload",
        "📊 ATS Score",
        "💼 Job Match",
        "🧠 Interview Generator",
        "📅 Learning Roadmap",
        "🤖 AI Chatbot"
    ]
)

# ===================================================
# HOME
# ===================================================

if page == "🏠 Home":

    st.title("🎯 AI Career Mentor")

    st.markdown("""
Welcome to **AI Career Mentor**.

This application helps students to:

- 📄 Upload Resume
- 📊 Check ATS Score
- 💼 Match Resume with Job Description
- 🧠 Generate Interview Questions
- 📅 Build Learning Roadmap
- 🤖 Chat with AI Career Mentor
""")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.success("📄 Resume Upload")

    with c2:
        st.success("📊 ATS Checker")

    with c3:
        st.success("💼 Job Matcher")

    c4, c5, c6 = st.columns(3)

    with c4:
        st.success("🧠 Interview Questions")

    with c5:
        st.success("📅 Learning Roadmap")

    with c6:
        st.success("🤖 AI Chatbot")

# ===================================================
# RESUME UPLOAD
# ===================================================

elif page == "📄 Resume Upload":

    st.title("📄 Resume Upload")

    uploaded_file = st.file_uploader(
        "Upload Resume (PDF)",
        type=["pdf"]
    )

    if uploaded_file is not None:

        try:

            resume_text = read_resume(uploaded_file)

            resume_data = parse_resume(resume_text)

            st.session_state.resume_text = resume_text
            st.session_state.resume_data = resume_data

            st.success("Resume Uploaded Successfully!")

            st.subheader("Candidate Information")

            col1, col2 = st.columns(2)

            with col1:

                st.markdown("### 👤 Name")
                st.success(resume_data.get("Name", "Not Found"))

                st.markdown("### 📧 Email")
                st.success(resume_data.get("Email", "Not Found"))

                st.markdown("### 📱 Phone")
                st.success(resume_data.get("Phone", "Not Found"))

            with col2:

                st.markdown("### 💻 Skills")

                skills = resume_data.get("Skills", [])

                if skills:
                    for skill in skills:
                        st.success(skill)
                else:
                    st.warning("No Skills Found")

            st.subheader("Extracted Resume Text")

            st.text_area(
                "",
                resume_text,
                height=350
            )

        except Exception as e:
            st.error(e)

# ===================================================
# ATS SCORE
# ===================================================

elif page == "📊 ATS Score":

    st.title("📊 ATS Resume Checker")

    if st.session_state.resume_data == {}:

        st.warning("Please upload your resume first.")

    else:

        result = calculate_ats(
            st.session_state.resume_data["Skills"]
        )

        st.subheader("ATS Score")

        st.progress(result["ATS Score"] / 100)

        st.success(
            f"ATS Score : {result['ATS Score']} / 100"
        )

        col1, col2 = st.columns(2)

        with col1:

            st.subheader("✅ Matching Skills")

            if result["Matched Skills"]:

                for skill in result["Matched Skills"]:
                    st.success(skill)

            else:

                st.warning("No Matching Skills")

        with col2:

            st.subheader("❌ Missing Skills")

            if result["Missing Skills"]:

                for skill in result["Missing Skills"]:
                    st.error(skill)

            else:

                st.success("No Missing Skills")

        st.markdown("---")

        st.subheader("💡 Suggestions")

        if result["Suggestions"]:

            for tip in result["Suggestions"]:
                st.info(tip)

        else:

            st.success("Your resume is well optimized.")

# ===================================================
# JOB MATCH
# ===================================================

elif page == "💼 Job Match":

    st.title("💼 Resume vs Job Description")

    if st.session_state.resume_data == {}:

        st.warning("Please upload your resume first.")

    else:

        jd = st.text_area(
            "Paste Job Description",
            height=250
        )

        if st.button("Match Resume"):

            if jd.strip() == "":
                st.warning("Enter Job Description")

            else:

                result = job_match(
                    st.session_state.resume_data["Skills"],
                    jd
                )

                st.subheader("Match Score")

                st.progress(result["Match Score"] / 100)

                st.success(
                    f"Match Score : {result['Match Score']}%"
                )

                col1, col2 = st.columns(2)

                with col1:

                    st.subheader("✅ Matched Skills")

                    if result["Matched Skills"]:

                        for skill in result["Matched Skills"]:
                            st.success(skill)

                    else:
                        st.warning("No Matched Skills")

                with col2:

                    st.subheader("❌ Missing Skills")

                    if result["Missing Skills"]:

                        for skill in result["Missing Skills"]:
                            st.error(skill)

                    else:
                        st.success("No Missing Skills")

                st.markdown("---")

                st.subheader("💡 Recommendations")

                if result["Suggestions"]:

                    for tip in result["Suggestions"]:
                        st.info(tip)

                else:
                    st.success("Excellent Resume!")

# ===================================================
# INTERVIEW GENERATOR
# ===================================================

elif page == "🧠 Interview Generator":

    st.title("🧠 AI Interview Question Generator")

    if st.session_state.resume_text == "":

        st.warning("Please upload your resume first.")

    else:

        st.write("Generate AI-based interview questions.")

        if st.button("Generate Questions"):

            with st.spinner("Generating..."):

                try:

                    questions = generate_interview_questions(
                        st.session_state.resume_text
                    )

                    st.markdown(questions)

                except Exception as e:

                    st.error(e)

# ===================================================
# ROADMAP
# ===================================================

elif page == "📅 Learning Roadmap":

    st.title("📅 AI Learning Roadmap")

    if st.session_state.resume_text == "":

        st.warning("Please upload your resume first.")

    else:

        if st.button("Generate Roadmap"):

            with st.spinner("Generating Roadmap..."):

                try:

                    roadmap = generate_roadmap(
                        st.session_state.resume_text
                    )

                    st.markdown(roadmap)

                except Exception as e:

                    st.error(e)

# ===================================================
# CHATBOT
# ===================================================

elif page == "🤖 AI Chatbot":

    st.title("🤖 AI Career Mentor Chatbot")

    if st.session_state.resume_text == "":

        st.warning("Please upload your resume first.")

    else:

        question = st.text_input(
            "Ask your career question"
        )

        if st.button("Ask AI"):

            if question.strip() == "":
                st.warning("Enter your question.")

            else:

                with st.spinner("Thinking..."):

                    try:

                        answer = chat_with_ai(
                            st.session_state.resume_text,
                            question
                        )

                        st.markdown(answer)

                    except Exception as e:

                        st.error(e)

# ===================================================
# FOOTER
# ===================================================

st.markdown("---")

st.caption(
    "🎯 AI Career Mentor | Built with Streamlit + Python + Google Gemini AI"
)