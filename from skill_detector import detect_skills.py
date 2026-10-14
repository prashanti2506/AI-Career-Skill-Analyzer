from skill_detector import detect_skills
from job_database import job_skills

print("================================")
print("   AI CAREER SKILL ANALYZER")
print("================================")

# Get user information
name = input("Enter your name: ")
target_job = input("Enter your target job: ")

# Get resume text
print("\nPaste your resume text below.")
print("When finished, type END on a new line.")

resume_lines = []

while True:
    line = input()

    if line.strip().upper() == "END":
        break

    resume_lines.append(line)

resume_text = " ".join(resume_lines)

# Detect skills from resume
skills = detect_skills(resume_text)

print("\n================================")
print("       DETECTED SKILLS")
print("================================")

if len(skills) == 0:
    print("No skills detected.")
else:
    for skill in skills:
        print("✓", skill)


# Clean target job
job = target_job.strip().lower()


# Check whether job exists
if job in job_skills:

    required_skills = job_skills[job]

    matched_skills = []
    missing_skills = []

    # Compare skills
    for skill in required_skills:

        if skill in skills:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    # Calculate match percentage
    match_percentage = (
        len(matched_skills) / len(required_skills)
    ) * 100

    # Job analysis
    print("\n================================")
    print("         JOB ANALYSIS")
    print("================================")

    print("Name:", name)
    print("Target Job:", target_job)

    print("\nMatched Skills:")

    for skill in matched_skills:
        print("✓", skill)

    print("\nMissing Skills:")

    for skill in missing_skills:
        print("✗", skill)

    print("\nJob Match:", round(match_percentage, 2), "%")


    # Match level
    if match_percentage >= 80:
        match_level = "Excellent Match"

    elif match_percentage >= 60:
        match_level = "Good Match"

    elif match_percentage >= 40:
        match_level = "Needs Improvement"

    else:
        match_level = "Beginner Level"

    print("Match Level:", match_level)


    # What to learn
    print("\n================================")
    print("     WHAT YOU SHOULD LEARN")
    print("================================")

    if len(missing_skills) == 0:

        print("You have all the required skills!")

    else:

        for i, skill in enumerate(missing_skills, start=1):
            print(f"{i}. {skill}")


    # Learning roadmap
    learning_order = {
        "python": "Learn Python fundamentals and OOP",
        "sql": "Learn SQL queries, joins, and databases",
        "git": "Learn Git commands and GitHub workflow",
        "flask": "Learn Flask and build a simple REST API",
        "django": "Learn Django and build a web application",
        "rest api": "Learn REST APIs and create APIs using Python",
        "docker": "Learn Docker basics and containerize a Python application",
        "pandas": "Learn Pandas for data cleaning and analysis",
        "numpy": "Learn NumPy arrays and numerical operations",
        "machine learning": "Learn machine learning algorithms and model evaluation",
        "statistics": "Learn probability and statistics for data science",
        "html": "Learn HTML structure and semantic elements",
        "css": "Learn CSS layouts and responsive design",
        "javascript": "Learn JavaScript fundamentals",
        "react": "Learn React components, state, and props",
        "java": "Learn Java fundamentals and object-oriented programming",
        "c": "Learn C programming fundamentals"
    }

    print("\n================================")
    print("       LEARNING ROADMAP")
    print("================================")

    if len(missing_skills) == 0:

        print("No additional skills required!")

    else:

        for i, skill in enumerate(missing_skills, start=1):

            print(f"\n{i}. {skill.upper()}")

            if skill in learning_order:
                print("   →", learning_order[skill])

            else:
                print("   → Find a course or tutorial for this skill.")


else:

    print("\nSorry, this job is not available.")

    print("\nAvailable jobs:")

    for available_job in job_skills:
        print("-", available_job.title())