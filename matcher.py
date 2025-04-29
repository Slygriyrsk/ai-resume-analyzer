# from sentence_transformers import SentenceTransformer
# from sklearn.metrics.pairwise import cosine_similarity
# import numpy as np
# import spacy
# import os
# from dotenv import load_dotenv

# nlp = spacy.load("en_core_web_sm")
# load_dotenv()
# model = SentenceTransformer("all-MiniLM-L6-v2")

# # In-memory cache for embeddings
# embedding_cache = {}

# def get_embedding_from_cache(text):
#     return embedding_cache.get(text)

# def cache_embedding(text, embedding):
#     embedding_cache[text] = embedding

# def get_embeddings(texts):
#     embeddings = []
#     for text in texts:
#         cached = get_embedding_from_cache(text)
#         if cached is not None:
#             embeddings.append(cached)
#         else:
#             embedding = model.encode([text], convert_to_tensor=False)[0]
#             cache_embedding(text, embedding)
#             embeddings.append(embedding)
#     return np.array(embeddings)

# def match_resume_to_job(resume_sections, job_description):
#     try:
#         resume_text = " ".join(sum([resume_sections[key] for key in resume_sections], []))
#         job_text = job_description
        
#         # Generate embeddings
#         embeddings = get_embeddings([resume_text, job_text])
#         similarity = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
        
#         # Extract skills
#         job_doc = nlp(job_description)
#         job_skills = [ent.text for ent in job_doc.ents if ent.label_ in ["SKILL", "NORP"]]
#         resume_skills = resume_sections["skills"]
        
#         missing_skills = [skill for skill in job_skills if skill.lower() not in [s.lower() for s in resume_skills]]
        
#         return {
#             "match_score": float(similarity),
#             "missing_skills": missing_skills
#         }
#     except Exception as e:
#         raise Exception(f"Error in matching: {str(e)}")

# from sentence_transformers import SentenceTransformer
# from sklearn.metrics.pairwise import cosine_similarity
# import numpy as np
# import spacy
# import os
# from dotenv import load_dotenv
# import logging

# # Configure logging
# logging.basicConfig(filename="app.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# nlp = spacy.load("en_core_web_sm")
# load_dotenv()
# model = SentenceTransformer("all-MiniLM-L6-v2")

# # In-memory cache for embeddings
# embedding_cache = {}
# MAX_CACHE_SIZE = 1000  # Limit cache size

# def get_embedding_from_cache(text):
#     return embedding_cache.get(text)

# def cache_embedding(text, embedding):
#     if len(embedding_cache) >= MAX_CACHE_SIZE:
#         embedding_cache.pop(next(iter(embedding_cache)))  # Remove oldest entry
#     embedding_cache[text] = embedding

# def get_embeddings(texts):
#     embeddings = []
#     for text in texts:
#         cached = get_embedding_from_cache(text)
#         if cached is not None:
#             embeddings.append(cached)
#             logging.info(f"Retrieved embedding from cache for text: {text[:50]}...")
#         else:
#             embedding = model.encode([text], convert_to_tensor=False)[0]
#             cache_embedding(text, embedding)
#             embeddings.append(embedding)
#             logging.info(f"Generated new embedding for text: {text[:50]}...")
#     return np.array(embeddings)

# def extract_keywords(text):
#     """Extract keywords (nouns, proper nouns, adjectives) as proxy for skills."""
#     doc = nlp(text)
#     keywords = [token.text.lower() for token in doc if token.pos_ in ["NOUN", "PROPN", "ADJ"]]
#     logging.info(f"Extracted keywords: {keywords[:10]}...")
#     return keywords

# def match_resume_to_job(resume_sections, job_description):
#     try:
#         # Combine resume sections into text
#         resume_text = " ".join(sum([resume_sections[key] for key in resume_sections if isinstance(resume_sections[key], list)], []))
#         job_text = job_description
        
#         # Generate embeddings
#         embeddings = get_embeddings([resume_text, job_text])
#         similarity = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
        
#         # Extract skills/keywords
#         job_keywords = extract_keywords(job_description)
#         resume_skills = [skill.lower() for skill in resume_sections.get("skills", [])]
        
#         missing_skills = [keyword for keyword in job_keywords if keyword not in resume_skills]
        
#         result = {
#             "match_score": float(similarity),
#             "missing_skills": missing_skills[:10]  # Limit to 10 for brevity
#         }
#         logging.info(f"Match result: {result}")
#         return result
#     except Exception as e:
#         logging.error(f"Error in matching: {str(e)}")
#         raise Exception(f"Error in matching: {str(e)}")

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import spacy
import os
from dotenv import load_dotenv
import logging

# Configure logging
logging.basicConfig(filename="app.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

nlp = spacy.load("en_core_web_sm")
load_dotenv()
model = SentenceTransformer("all-MiniLM-L6-v2")

# Predefined skill list
SKILL_LIST = [
    "python", "aws", "docker", "mongodb", "postgresql", "git", "streamlit",
    "react", "node.js", "flask", "sql", "javascript", "html", "css",
    "machine learning", "data analysis", "cloud computing"
]

# In-memory cache for embeddings
embedding_cache = {}
MAX_CACHE_SIZE = 1000

def get_embedding_from_cache(text):
    return embedding_cache.get(text)

def cache_embedding(text, embedding):
    if len(embedding_cache) >= MAX_CACHE_SIZE:
        embedding_cache.pop(next(iter(embedding_cache)))
    embedding_cache[text] = embedding

def get_embeddings(texts):
    embeddings = []
    for text in texts:
        cached = get_embedding_from_cache(text)
        if cached is not None:
            embeddings.append(cached)
            logging.info(f"Retrieved embedding from cache for text: {text[:50]}...")
        else:
            embedding = model.encode([text], convert_to_tensor=False)[0]
            cache_embedding(text, embedding)
            embeddings.append(embedding)
            logging.info(f"Generated new embedding for text: {text[:50]}...")
    return np.array(embeddings)

def extract_keywords(text):
    doc = nlp(text.lower())
    keywords = [token.text for token in doc if token.text in SKILL_LIST]
    logging.info(f"Extracted keywords: {keywords[:10]}...")
    return keywords

def match_resume_to_job(resume_sections, job_description):
    try:
        resume_text = " ".join(sum([resume_sections[key] for key in resume_sections if isinstance(resume_sections[key], list)], []))
        job_text = job_description
        
        embeddings = get_embeddings([resume_text, job_text])
        similarity = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
        
        job_keywords = extract_keywords(job_description)
        resume_skills = [skill.lower() for skill in resume_sections.get("skills", [])]
        
        missing_skills = [keyword for keyword in job_keywords if keyword not in resume_skills]
        
        result = {
            "match_score": float(similarity),
            "missing_skills": missing_skills[:10]
        }
        logging.info(f"Match result: {result}")
        return result
    except Exception as e:
        logging.error(f"Error in matching: {str(e)}")
        raise Exception(f"Error in matching: {str(e)}")