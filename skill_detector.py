import re

# Skills our program can detect
skill_list = [
    "python",
    "java",
    "c",
    "c++",
    "sql",
    "git",
    "github",
    "flask",
    "django",
    "rest api",
    "docker",
    "pandas",
    "numpy",
    "machine learning",
    "statistics",
    "html",
    "css",
    "javascript",
    "react"
]


def detect_skills(resume_text):

    detected_skills = []

    resume_text = resume_text.lower()

    for skill in skill_list:

        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern, resume_text):
            detected_skills.append(skill)

    return detected_skills