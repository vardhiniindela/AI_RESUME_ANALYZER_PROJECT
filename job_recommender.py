from skills import skills_db

def recommend_jobs(user_skills):
    recommendations = {}

    for role, skills in skills_db.items():
        match = len(set(user_skills) & set(skills))
        score = int((match / len(skills)) * 100)
        recommendations[role] = score

    return recommendations