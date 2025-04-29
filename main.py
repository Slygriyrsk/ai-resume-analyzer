# from fastapi import FastAPI, UploadFile, File, HTTPException
# from pydantic import BaseModel
# from resume_parser import parse_resume
# from matcher import match_resume_to_job
# from ats_scorer import compute_ats_score
# from improvement_tips import generate_improvement_tips, rewrite_bullet_points
# from learning_paths import get_learning_paths
# from interview_prep import generate_interview_prep
# import os

# app = FastAPI()

# class JobDescription(BaseModel):
#     text: str

# @app.post("/analyze")
# async def analyze_resume(file: UploadFile = File(...), job: JobDescription = None):
#     if not file.filename.endswith((".pdf", ".docx")):
#         raise HTTPException(status_code=400, detail="Invalid file format")
    
#     # Save uploaded file temporarily
#     temp_path = f"temp_{file.filename}"
#     with open(temp_path, "wb") as f:
#         f.write(await file.read())
    
#     try:
#         # Parse resume
#         resume_sections = parse_resume(temp_path)
        
#         # Match to job description
#         job_description = job.text if job else "Software Engineer role requiring Python, AWS, Docker."
#         match_result = match_resume_to_job(resume_sections, job_description)
        
#         # Compute ATS score
#         ats_result = compute_ats_score(resume_sections, job_description)
        
#         # Generate improvement tips
#         tips = generate_improvement_tips(resume_sections, job_description, match_result["missing_skills"])
        
#         # Rewrite weak bullet points
#         rewritten_bullets = rewrite_bullet_points(resume_sections)
        
#         # Generate learning paths
#         learning_paths = get_learning_paths(match_result["missing_skills"])
        
#         # Generate interview prep
#         interview_questions = generate_interview_prep(resume_sections, job_description, match_result["missing_skills"])
        
#         return {
#             "resume_sections": resume_sections,
#             "match_score": match_result["match_score"],
#             "missing_skills": match_result["missing_skills"],
#             "ats_score": ats_result["ats_score"],
#             "ats_details": ats_result["details"],
#             "improvement_tips": tips,
#             "rewritten_bullets": rewritten_bullets,
#             "learning_paths": learning_paths,
#             "interview_questions": interview_questions
#         }
#     finally:
#         # Ensure temporary file is deleted
#         if os.path.exists(temp_path):
#             os.remove(temp_path)

from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
from resume_parser import parse_resume
from matcher import match_resume_to_job
from ats_scorer import compute_ats_score
from improvement_tips import generate_improvement_tips, rewrite_bullet_points
from learning_paths import get_learning_paths
from interview_prep import generate_interview_prep
import os
import logging

# Configure logging
logging.basicConfig(filename="app.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

app = FastAPI()

class JobDescription(BaseModel):
    text: str

def truncate_text(text, max_chars=500):
    """Truncate text to max_chars."""
    if isinstance(text, str):
        return text[:max_chars]
    return str(text)[:max_chars]

def validate_resume_sections(sections):
    """Validate and truncate resume_sections."""
    if not isinstance(sections, dict):
        logging.error("Invalid resume_sections format")
        raise HTTPException(status_code=500, detail="Invalid resume format")
    
    result = {}
    for key in ["skills", "experience", "education"]:
        value = sections.get(key, [])
        if not isinstance(value, list):
            value = [str(value)]
        result[key] = [truncate_text(item, 200) for item in value[:5]]  # Limit to 5 items
    logging.info(f"Validated resume_sections: {result}")
    return result

@app.post("/analyze")
async def analyze_resume(file: UploadFile = File(...), job: JobDescription = None):
    if not file.filename.endswith((".pdf", ".docx")):
        raise HTTPException(status_code=400, detail="Invalid file format")
    
    # Save uploaded file temporarily
    temp_path = f"temp_{file.filename}"
    with open(temp_path, "wb") as f:
        f.write(await file.read())
    
    try:
        # Parse resume
        resume_sections = parse_resume(temp_path)
        resume_sections = validate_resume_sections(resume_sections)
        
        # Truncate job description
        job_description = job.text if job else "Software Engineer role requiring Python, AWS, Docker."
        job_description = truncate_text(job_description, 500)
        logging.info(f"Job description length: {len(job_description)} chars")
        
        # Match to job description
        match_result = match_resume_to_job(resume_sections, job_description)
        
        # Compute ATS score
        ats_result = compute_ats_score(resume_sections, job_description)
        
        # Generate improvement tips
        tips = generate_improvement_tips(resume_sections, job_description, match_result["missing_skills"])
        
        # Rewrite weak bullet points
        rewritten_bullets = rewrite_bullet_points(resume_sections)
        
        # Generate learning paths
        learning_paths = get_learning_paths(match_result["missing_skills"])
        
        # Generate interview prep
        interview_questions = generate_interview_prep(resume_sections, job_description, match_result["missing_skills"])
        
        return {
            "resume_sections": resume_sections,
            "match_score": match_result["match_score"],
            "missing_skills": match_result["missing_skills"],
            "ats_score": ats_result["ats_score"],
            "ats_details": ats_result["details"],
            "improvement_tips": tips,
            "rewritten_bullets": rewritten_bullets,
            "learning_paths": learning_paths,
            "interview_questions": interview_questions
        }
    except Exception as e:
        logging.error(f"Error in /analyze: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        # Ensure temporary file is deleted
        if os.path.exists(temp_path):
            os.remove(temp_path)