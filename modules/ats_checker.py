class ATSChecker:

    def __init__(self, resume_skills):

        self.resume_skills = resume_skills

        self.required_skills = [

            "Python",
            "Java",
            "SQL",
            "HTML",
            "CSS",
            "JavaScript",

            "Machine Learning",
            "Deep Learning",
            "Artificial Intelligence",
            "Data Science",

            "Pandas",
            "NumPy",
            "Scikit-learn",
            "TensorFlow",

            "Git",
            "GitHub",

            "Power BI",
            "Excel",

            "Streamlit",
            "Flask",

            "NLP",
            "Computer Vision",
            "Generative AI"
        ]

    def matched_skills(self):

        matched = []

        for skill in self.required_skills:

            if skill in self.resume_skills:
                matched.append(skill)

        return matched

    def missing_skills(self):

        missing = []

        for skill in self.required_skills:

            if skill not in self.resume_skills:
                missing.append(skill)

        return missing

    def calculate_score(self):

        matched = self.matched_skills()

        total = len(self.required_skills)

        score = int((len(matched) / total) * 100)

        return score

    def improvement_tips(self):

        tips = []

        missing = self.missing_skills()

        if "Python" in missing:
            tips.append("Learn Python Programming")

        if "SQL" in missing:
            tips.append("Practice SQL Queries")

        if "Git" in missing:
            tips.append("Learn Git & GitHub")

        if "Machine Learning" in missing:
            tips.append("Complete a Machine Learning Project")

        if "Deep Learning" in missing:
            tips.append("Learn TensorFlow or PyTorch")

        if "Streamlit" in missing:
            tips.append("Build Streamlit Projects")

        if "Power BI" in missing:
            tips.append("Learn Power BI Dashboard")

        return tips

    def get_result(self):

        return {

            "ATS Score": self.calculate_score(),

            "Matched Skills": self.matched_skills(),

            "Missing Skills": self.missing_skills(),

            "Suggestions": self.improvement_tips()
        }


def calculate_ats(resume_skills):

    checker = ATSChecker(resume_skills)

    return checker.get_result()