import re


class JobMatcher:

    def __init__(self, resume_skills, job_description):

        self.resume_skills = resume_skills
        self.job_description = job_description.lower()

    def extract_job_skills(self):

        skills_database = [

            "Python",
            "Java",
            "C",
            "C++",
            "SQL",
            "MySQL",

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
            "PyTorch",

            "Git",
            "GitHub",

            "Power BI",
            "Excel",

            "Streamlit",
            "Flask",

            "NLP",
            "Computer Vision",

            "Generative AI",

            "OpenCV",

            "MongoDB"
        ]

        found = []

        for skill in skills_database:

            if skill.lower() in self.job_description:
                found.append(skill)

        return sorted(list(set(found)))

    def matched_skills(self):

        matched = []

        job_skills = self.extract_job_skills()

        for skill in job_skills:

            if skill in self.resume_skills:
                matched.append(skill)

        return matched

    def missing_skills(self):

        missing = []

        job_skills = self.extract_job_skills()

        for skill in job_skills:

            if skill not in self.resume_skills:
                missing.append(skill)

        return missing

    def match_score(self):

        job_skills = self.extract_job_skills()

        if len(job_skills) == 0:
            return 0

        score = int((len(self.matched_skills()) / len(job_skills)) * 100)

        return score

    def suggestions(self):

        tips = []

        for skill in self.missing_skills():

            tips.append(f"Learn {skill}")

        return tips

    def get_result(self):

        return {

            "Match Score": self.match_score(),

            "Job Skills": self.extract_job_skills(),

            "Matched Skills": self.matched_skills(),

            "Missing Skills": self.missing_skills(),

            "Suggestions": self.suggestions()
        }


def job_match(resume_skills, job_description):

    matcher = JobMatcher(resume_skills, job_description)

    return matcher.get_result()