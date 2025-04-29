import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Expanded skills and action verbs
SKILLS = ["Python", "Java", "AWS", "Docker", "SQL", "Kubernetes", "JavaScript", "React", "Node.js", "TensorFlow", "C++", "Ruby"]
ACTION_VERBS = ["developed", "led", "built", "designed", "implemented", "optimized", "managed", "deployed", "tested", "integrated"]
FILLER_WORDS = ["team", "project", "system", "application", "scalable", "robust", "innovative", "collaborative", "efficient"]

def generate_resume(num_skills=3, num_experiences=2, has_skills_section=True):
    # Randomly select skills, with some unrelated to job
    all_skills = SKILLS + ["Excel", "Photoshop", "Marketing"]  # Add noise skills
    skills = np.random.choice(all_skills, size=min(num_skills, len(all_skills)), replace=False)
    experiences = [
        f"{np.random.choice(ACTION_VERBS)} {np.random.choice(FILLER_WORDS)} {np.random.choice(['application', 'system', 'pipeline', 'tool'])} using {np.random.choice(all_skills)}"
        for _ in range(num_experiences)
    ]
    # Add random filler text for realism
    filler = " ".join(np.random.choice(FILLER_WORDS + ["data", "analysis", "strategy"], size=np.random.randint(10, 20)))
    resume = []
    if has_skills_section:
        resume.append("Skills: " + ", ".join(skills))
    resume.append("Experience: " + "; ".join(experiences))
    resume.append(f"Additional: {filler}")
    # Randomly vary length
    if np.random.random() < 0.3:
        resume.append("Extra: " + " ".join(np.random.choice(FILLER_WORDS, size=np.random.randint(5, 15))))
    return " ".join(resume)

def generate_job_description(num_skills=4):
    skills = np.random.choice(SKILLS, size=min(num_skills, len(SKILLS)), replace=False)
    filler = " ".join(np.random.choice(FILLER_WORDS, size=np.random.randint(5, 15)))
    return f"Software Engineer role requiring expertise in {', '.join(skills)} and experience in building {filler} systems."

def compute_features(resume, job_description):
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform([resume, job_description])
    keyword_score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    length = len(resume.split())
    has_skills_section = 1 if "Skills:" in resume else 0
    action_verbs = sum(1 for verb in ACTION_VERBS if verb in resume.lower())
    return keyword_score, length, has_skills_section, action_verbs

def generate_synthetic_dataset(n_samples=1000):
    data = []
    for _ in range(n_samples):
        num_skills = np.random.randint(1, 8)
        num_experiences = np.random.randint(1, 6)
        has_skills_section = np.random.choice([True, False], p=[0.6, 0.4])
        resume = generate_resume(num_skills, num_experiences, has_skills_section)
        job_description = generate_job_description(num_skills=np.random.randint(2, 6))
        keyword_score, length, has_skills_section, action_verbs = compute_features(resume, job_description)
        
        # More nuanced labeling with increased noise
        score = (
            keyword_score * 0.4 +
            (length / 600) * 0.2 +  # Normalize length
            has_skills_section * 0.2 +
            (action_verbs / 6) * 0.2
        )
        # Increase noise for less deterministic labels
        label = 1 if score > 0.6 + np.random.uniform(-0.2, 0.2) else 0
        
        data.append({
            "resume_text": resume,
            "job_description": job_description,
            "keyword_score": keyword_score,
            "length": length,
            "has_skills_section": has_skills_section,
            "action_verbs": action_verbs,
            "label": label
        })
    return pd.DataFrame(data)

if __name__ == "__main__":
    dataset = generate_synthetic_dataset(1000)
    dataset.to_csv("data/synthetic_ats_data.csv", index=False)
    print("Synthetic dataset generated and saved to data/synthetic_ats_data.csv")
    print("Label distribution:")
    print(dataset["label"].value_counts(normalize=True))