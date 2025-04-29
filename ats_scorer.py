import pickle
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load trained model and vectorizer
with open("models/ats_model.pkl", "rb") as f:
    ats_model = pickle.load(f)
with open("models/tfidf_vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

def compute_ats_score(resume_sections, job_description):
    resume_text = " ".join(sum([resume_sections[key] for key in resume_sections], []))
    
    # Rule-based score
    score = 0
    if len(resume_text.split()) > 100:
        score += 20
    if any("skills" in s.lower() for s in resume_sections):
        score += 20
    if any(re.search(r"developed|led|built", s.lower()) for s in resume_sections["experience"]):
        score += 15
    
    # ML-based score
    tfidf_matrix = vectorizer.transform([resume_text, job_description])
    keyword_score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0] * 45
    features = [
        keyword_score,
        len(resume_text.split()),
        1 if any("skills" in s.lower() for s in resume_sections) else 0,
        sum(1 for s in resume_sections["experience"] if re.search(r"developed|led|built", s.lower()))
    ]
    ml_score = ats_model.predict_proba([features])[0][1] * 100
    
    final_score = min((score + ml_score) / 2, 100)
    
    return {
        "ats_score": final_score,
        "details": {
            "keyword_match": keyword_score,
            "section_clarity": 20 if "skills" in resume_sections else 0,
            "action_verbs": 15 if any(re.search(r"developed|led|built", s.lower()) for s in resume_sections["experience"]) else 0
        }
    }