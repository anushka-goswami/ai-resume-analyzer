import pdfplumber
import re
from job_match import match_resume_with_job

from skill_analyzer import (
    detect_skills,
    calculate_ats_score,
    get_missing_skills,
    generate_suggestions
)

def extract_text_from_pdf(pdf_path):
    text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + " "

    return text


def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    text = text.lower()
    return text


if __name__ == "__main__":
    text = extract_text_from_pdf("resume.pdf")
    text = clean_text(text)
    print(text)

from skill_analyzer import detect_skills, calculate_ats_score

if __name__ == "__main__":

    text = extract_text_from_pdf("resume.pdf")
    text = clean_text(text)

    skills_found = detect_skills(text)
    score = calculate_ats_score(skills_found)

    print("Skills Found:", skills_found)
    print("ATS Score:", score)

if __name__ == "__main__":

    text = extract_text_from_pdf("resume.pdf")
    text = clean_text(text)

    job_desc = """
    Looking for python developer with knowledge of machine learning,
    nodejs, and web development.
    """

    from skill_analyzer import detect_skills, calculate_ats_score

    skills_found = detect_skills(text)
    score = calculate_ats_score(skills_found)

    match_score = match_resume_with_job(job_desc, text)

    print("Skills Found:", skills_found)
    print("ATS Score:", score)
    print("Job Match Score:", match_score)

if __name__ == "__main__":

    text = extract_text_from_pdf("resume.pdf")
    text = clean_text(text)

    job_desc = """
    Looking for python developer with machine learning,
    nodejs and web development knowledge.
    """

    skills_found = detect_skills(text)
    score = calculate_ats_score(skills_found)

    missing_skills = get_missing_skills(skills_found)
    suggestions = generate_suggestions(missing_skills)

    match_score = match_resume_with_job(job_desc, text)

    print("\nSkills Found:", skills_found)
    print("\nATS Score:", score)
    print("\nJob Match Score:", match_score)
    print("\nMissing Skills:", missing_skills)
    print("\nSuggestions:")
    
    for s in suggestions:
        print("-", s)