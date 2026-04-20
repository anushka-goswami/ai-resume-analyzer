from flask import Flask, request, jsonify
from flask_cors import CORS

from resume_extract import *
from skill_analyzer import *
from job_match import *

import os

app = Flask(__name__)
CORS(app)

# Ensure uploads folder exists
if not os.path.exists("uploads"):
    os.makedirs("uploads")


# ⭐ FREE Suggestion Generator (Rule-Based AI Style)
def generate_suggestions(text):

    suggestions = []
    text_lower = text.lower()

    # Section checks
    if "project" not in text_lower:
        suggestions.append("Add more project details with measurable outcomes.")

    if "internship" not in text_lower:
        suggestions.append("Include internship or practical experience if available.")

    if "education" not in text_lower:
        suggestions.append("Clearly mention your education details.")

    # Length check
    if len(text.split()) < 300:
        suggestions.append("Resume appears short. Add more technical depth and descriptions.")

    # Skill presence checks
    if "github" not in text_lower:
        suggestions.append("Add GitHub or portfolio links to showcase your work.")

    if "machine learning" in text_lower and "project" not in text_lower:
        suggestions.append("Mention specific Machine Learning projects with tools used.")

    # Always helpful improvements
    suggestions.append("Quantify achievements using numbers (e.g., improved efficiency by 30%).")
    suggestions.append("Keep formatting clean, consistent, and ATS-friendly.")

    return suggestions


@app.route("/")
def home():
    return "ML Resume Analyzer Server Running 🚀"


@app.route("/analyze", methods=["POST"])
def analyze_resume():

    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    file_path = os.path.join("uploads", file.filename)
    file.save(file_path)

    # Extract + Clean
    text = extract_text_from_pdf(file_path)
    text = clean_text(text)

    # Skill Analysis
    skills_found = detect_skills(text)
    score = calculate_ats_score(skills_found)

    # Job Matching
    job_desc = "python machine learning web development"
    match_score = match_resume_with_job(job_desc, text)

    # Suggestions (FREE AI-style)
    suggestions = generate_suggestions(text)

    return jsonify({
        "skills": skills_found,
        "ats_score": score,
        "match_score": match_score,
        "suggestions": suggestions
    })


if __name__ == "__main__":
    app.run(port=5000, debug=True)