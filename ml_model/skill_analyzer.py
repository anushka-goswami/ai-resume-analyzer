# Skill Database
skills_db = [
"python","java","javascript","react",
"nodejs","mongodb","sql","html","css",
"machine learning","ai","nlp","express"
]


# Skill Detection Function
def detect_skills(resume_text):

    found_skills = []

    for skill in skills_db:
        if skill in resume_text:
            found_skills.append(skill)

    return found_skills


# ATS Score Calculation
def calculate_ats_score(found_skills):

    total_skills = len(skills_db)

    if total_skills == 0:
        return 0

    score = (len(found_skills) / total_skills) * 100
    return round(score, 2)

def get_missing_skills(found_skills):

    missing_skills = []

    for skill in skills_db:
        if skill not in found_skills:
            missing_skills.append(skill)

    return missing_skills

def generate_suggestions(missing_skills):

    suggestions = []

    for skill in missing_skills:
        suggestions.append(f"Consider learning {skill} to improve your profile")

    return suggestions