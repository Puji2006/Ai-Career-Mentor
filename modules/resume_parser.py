import re

# ----------------------------
# Extract Email
# ----------------------------
def extract_email(text):
    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
    match = re.search(pattern, text)
    return match.group() if match else "Not Found"


# ----------------------------
# Extract Phone
# ----------------------------
def extract_phone(text):
    pattern = r"\+?\d[\d\s-]{8,}\d"
    match = re.search(pattern, text)
    return match.group() if match else "Not Found"


# ----------------------------
# Extract Name
# ----------------------------
def extract_name(text):
    lines = text.split("\n")

    for line in lines:
        line = line.strip()

        if len(line) > 2:
            return line

    return "Not Found"


# ----------------------------
# Extract Skills
# ----------------------------
def extract_skills(text):

    skills_database = [

        "Python",
        "Java",
        "C",
        "C++",
        "JavaScript",
        "HTML",
        "CSS",
        "SQL",

        "Machine Learning",
        "Deep Learning",
        "Artificial Intelligence",
        "Data Science",

        "Pandas",
        "NumPy",
        "Scikit-learn",
        "TensorFlow",
        "PyTorch",

        "Power BI",
        "Excel",

        "Git",
        "GitHub",

        "Streamlit",
        "Flask",

        "Generative AI",
        "NLP",
        "Computer Vision"
    ]

    found_skills = []

    text = text.lower()

    for skill in skills_database:

        if skill.lower() in text:
            found_skills.append(skill)

    return found_skills


# ----------------------------
# Main Parser
# ----------------------------
def parse_resume(text):

    return {

        "Name": extract_name(text),

        "Email": extract_email(text),

        "Phone": extract_phone(text),

        "Skills": extract_skills(text)
    }