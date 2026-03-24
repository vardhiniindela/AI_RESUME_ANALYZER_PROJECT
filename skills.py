skills_list = [
    "python", "java", "sql", "machine learning",
    "data analysis", "pandas", "numpy", "deep learning"
]

def extract_skills(text):
    found_skills = []

    for skill in skills_list:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    return found_skills

skills_db = {
    "Data Analyst": ["python", "sql", "excel", "pandas"],
    "ML Engineer": ["python", "machine learning", "numpy", "pandas"],
    "Web Developer": ["html", "css", "javascript", "django"]
}

def extract_skills(text):
    found = []

    for role in skills_db:
        for skill in skills_db[role]:
            if skill in text and skill not in found:
                found.append(skill)

    return found