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


# Display detected skills
print("\n================================")
print("       DETECTED SKILLS")
print("================================")

if len(skills) == 0:
    print("No skills detected.")
else:
    for skill in skills:
        print("✓", skill)


# Clean target job name
job = target_job.strip().lower()


# Check whether the job exists
if job in job_skills:

    required_skills = job_skills[job]

    matched_skills = []
    missing_skills = []


    # Compare user skills with required skills
    for skill in required_skills:

        if skill in skills:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)


    # Calculate job match percentage
    match_percentage = (
        len(matched_skills) / len(required_skills)
    ) * 100


    # Job analysis
    print("\n================================")
    print("         JOB ANALYSIS")
    print("================================")

    print("Name:", name)
    print("Target Job:", target_job)


    # Matched skills
    print("\nMatched Skills:")

    if len(matched_skills) == 0:
        print("No matching skills found.")
    else:
        for skill in matched_skills:
            print("✓", skill)


    # Missing skills
    print("\nMissing Skills:")

    if len(missing_skills) == 0:
        print("No missing skills!")
    else:
        for skill in missing_skills:
            print("✗", skill)


    # Display match percentage
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


    # Skill gap summary
    print("\n================================")
    print("        SKILL GAP SUMMARY")
    print("================================")

    if match_percentage >= 80:

        print("You are well prepared for this job.")

    elif match_percentage >= 60:

        print("You have a good foundation, but you need to improve some skills.")

    elif match_percentage >= 40:

        print("You have a basic foundation. Focus on the missing skills to become job-ready.")

    else:

        print("You need to build more skills before applying for this role.")


    # Skill priority
    print("\n================================")
    print("     WHAT YOU SHOULD LEARN")
    print("================================")


    if len(missing_skills) == 0:

        print("You have all the required skills!")

    else:

        priority = {
            "flask": 1,
            "django": 2,
            "rest api": 3,
            "docker": 4,

            "python": 1,
            "sql": 1,
            "git": 1,

            "html": 1,
            "css": 2,
            "javascript": 3,
            "react": 4,

            "java": 1,
            "c": 1,

            "pandas": 2,
            "numpy": 2,
            "statistics": 2,
            "machine learning": 3,

            "spring boot": 2,
            "maven": 2,
            "excel": 1
        }


        # Sort missing skills according to priority
        sorted_skills = sorted(
            missing_skills,
            key=lambda skill: priority.get(skill, 5)
        )


        for i, skill in enumerate(sorted_skills, start=1):

            print(f"{i}. {skill}")


    # Learning roadmap
    print("\n================================")
    print("       LEARNING ROADMAP")
    print("================================")


    learning_order = {

        "python":
            "Learn Python fundamentals, functions, OOP and file handling.",

        "java":
            "Learn Java fundamentals and object-oriented programming.",

        "c":
            "Learn C programming fundamentals, arrays, pointers and functions.",

        "sql":
            "Learn SQL queries, joins, subqueries and database concepts.",

        "git":
            "Learn Git commands, branches, commits and GitHub workflow.",

        "github":
            "Learn GitHub repositories, pull requests and collaboration.",

        "flask":
            "Learn Flask and build a simple REST API.",

        "django":
            "Learn Django and build a web application.",

        "rest api":
            "Learn REST API concepts and create APIs using Python.",

        "docker":
            "Learn Docker basics and containerize a Python application.",

        "pandas":
            "Learn Pandas for data cleaning, analysis and data processing.",

        "numpy":
            "Learn NumPy arrays and numerical operations.",

        "machine learning":
            "Learn machine learning algorithms and model evaluation.",

        "statistics":
            "Learn probability, statistics and data analysis.",

        "html":
            "Learn HTML structure, forms and semantic elements.",

        "css":
            "Learn CSS, layouts, Flexbox, Grid and responsive design.",

        "javascript":
            "Learn JavaScript fundamentals, DOM and events.",

        "react":
            "Learn React components, props, state and hooks.",

        "spring boot":
            "Learn Spring Boot and build Java backend applications.",

        "maven":
            "Learn Maven project management and dependency handling.",

        "excel":
            "Learn Excel formulas, charts, sorting and data analysis."
    }


    if len(missing_skills) == 0:

        print("\nNo additional skills required!")

    else:

        for i, skill in enumerate(sorted_skills, start=1):

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