from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def match_resume_with_job(job_desc, resume_text):

    # Convert text into vectors
    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform([job_desc, resume_text])

    similarity = cosine_similarity(vectors[0], vectors[1])

    return round(similarity[0][0] * 100, 2)