# from transformers import AutoModelForCausalLM, AutoTokenizer
# import torch
# from dotenv import load_dotenv
# import os

# load_dotenv()

# # Load local LLM
# model_name = "distilbert/distilgpt2"
# tokenizer = AutoTokenizer.from_pretrained(model_name)
# model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16, device_map="auto")

# def generate_improvement_tips(resume_sections, job_description, missing_skills):
#     prompt = f"""
#     Given the resume: {resume_sections}
#     And the job description: {job_description}
#     With missing skills: {', '.join(missing_skills)}
#     Provide 3 specific, actionable improvement tips to align the resume with the job.
#     """
    
#     inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
#     outputs = model.generate(
#         **inputs,
#         max_length=500,
#         num_return_sequences=1,
#         temperature=0.7,
#         do_sample=True
#     )
#     response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
#     # Extract tips
#     tips = response.split("\n")[:3]
#     return [tip.strip() for tip in tips if tip.strip()]

# def rewrite_bullet_points(resume_sections):
#     weak_bullets = [b for b in resume_sections["experience"] if len(b.split()) < 10 or "wrote" in b.lower()]
#     if not weak_bullets:
#         return []
    
#     rewritten = []
#     for bullet in weak_bullets[:2]:
#         prompt = f"Rewrite this resume bullet to be more impactful and professional: {bullet}"
#         inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
#         outputs = model.generate(
#             **inputs,
#             max_length=100,
#             num_return_sequences=1,
#             temperature=0.7,
#             do_sample=True
#         )
#         rewritten.append(tokenizer.decode(outputs[0], skip_special_tokens=True).strip())
    
#     return rewritten

# from sentence_transformers import SentenceTransformer
# from transformers import AutoModelForCausalLM, AutoTokenizer
# import torch
# from dotenv import load_dotenv
# import os

# load_dotenv()

# # Load local LLM
# model_name = "distilbert/distilgpt2"
# tokenizer = AutoTokenizer.from_pretrained(model_name)
# model = AutoModelForCausalLM.from_pretrained(model_name)

# def generate_improvement_tips(resume_sections, job_description, missing_skills):
#     prompt = f"""
#     Given the resume: {resume_sections}
#     And the job description: {job_description}
#     With missing skills: {', '.join(missing_skills)}
#     Provide 3 specific, actionable improvement tips to align the resume with the job.
#     """
    
#     # Limit prompt length
#     prompt = prompt[:2000]  # Cut characters to avoid too many tokens (2000 chars is roughly safe)

#     inputs = tokenizer(prompt, return_tensors="pt", truncation=True)
#     outputs = model.generate(
#         **inputs,
#         max_new_tokens=500,
#         num_return_sequences=1,
#         temperature=0.7,
#         do_sample=True
#     )
#     response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
#     # Extract tips
#     tips = response.split("\n")[:3]
#     return [tip.strip() for tip in tips if tip.strip()]


# def rewrite_bullet_points(resume_sections):
#     weak_bullets = [
#         b for b in resume_sections.get("experience", []) 
#         if len(b.split()) < 10 or "wrote" in b.lower()
#     ]
#     if not weak_bullets:
#         return []
    
#     rewritten = []
#     for bullet in weak_bullets[:2]:
#         prompt = f"Rewrite this resume bullet to be more impactful and professional: {bullet}"
#         inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512)
#         outputs = model.generate(
#             **inputs,
#             max_new_tokens=100,
#             num_return_sequences=1,
#             temperature=0.7,
#             do_sample=True
#         )
#         rewritten_bullet = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()
#         rewritten.append(rewritten_bullet)
    
#     return rewritten

# from transformers import AutoModelForCausalLM, AutoTokenizer
# import torch
# from dotenv import load_dotenv
# import os
# import logging

# # Configure logging
# logging.basicConfig(filename="app.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# load_dotenv()

# # Load local LLM
# model_name = "distilbert/distilgpt2"
# tokenizer = AutoTokenizer.from_pretrained(model_name)
# model = AutoModelForCausalLM.from_pretrained(model_name)

# def truncate_prompt(text, max_tokens=400):
#     """Truncate text to fit within max_tokens."""
#     try:
#         tokens = tokenizer.encode(text, truncation=True, max_length=max_tokens)
#         truncated_text = tokenizer.decode(tokens, skip_special_tokens=True)
#         logging.info(f"Truncated text to {len(tokens)} tokens: {truncated_text[:50]}...")
#         return truncated_text
#     except Exception as e:
#         logging.error(f"Error truncating prompt: {str(e)}")
#         return text[:100]  # Fallback to character-based truncation

# def generate_improvement_tips(resume_sections, job_description, missing_skills):
#     try:
#         # Summarize resume_sections
#         resume_summary = "Skills: " + ", ".join(resume_sections.get("skills", [])) + ". "
#         resume_summary += "Experience: " + " ".join(resume_sections.get("experience", [])[:2]) + ". "
#         resume_summary += "Education: " + " ".join(resume_sections.get("education", [])[:1])
        
#         # Truncate inputs
#         resume_text = truncate_prompt(resume_summary, max_tokens=150)
#         job_text = truncate_prompt(job_description, max_tokens=150)
#         skills_text = truncate_prompt(', '.join(missing_skills), max_tokens=50)

#         prompt = f"""
#         Resume: {resume_text}
#         Job: {job_text}
#         Missing Skills: {skills_text}
#         Provide 3 concise improvement tips to align the resume with the job.
#         """
        
#         # Ensure prompt fits within 400 tokens
#         prompt = truncate_prompt(prompt, max_tokens=400)
#         logging.info(f"Final prompt token count: {len(tokenizer.encode(prompt))}")

#         inputs = tokenizer(prompt, return_tensors="pt")
#         outputs = model.generate(
#             **inputs,
#             max_new_tokens=150,  # Reduced to stay under 1024 (400 input + 150 output + buffer)
#             num_return_sequences=1,
#             temperature=0.7,
#             do_sample=True
#         )
#         response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
#         # Extract tips
#         tips = response.split("\n")[:3]
#         return [tip.strip() for tip in tips if tip.strip()]
#     except Exception as e:
#         logging.error(f"Error generating tips: {str(e)}")
#         return ["Add relevant skills to your resume.", "Tailor experience to job requirements.", "Highlight achievements."]

# def rewrite_bullet_points(resume_sections):
#     try:
#         weak_bullets = [b for b in resume_sections.get("experience", []) if len(b.split()) < 10 or "wrote" in b.lower()]
#         if not weak_bullets:
#             return []
        
#         rewritten = []
#         for bullet in weak_bullets[:2]:
#             prompt = truncate_prompt(f"Rewrite this bullet to be impactful: {bullet}", max_tokens=150)
#             inputs = tokenizer(prompt, return_tensors="pt")
#             outputs = model.generate(
#                 **inputs,
#                 max_new_tokens=100,
#                 num_return_sequences=1,
#                 temperature=0.7,
#                 do_sample=True
#             )
#             rewritten.append(tokenizer.decode(outputs[0], skip_special_tokens=True).strip())
        
#         return rewritten
#     except Exception as e:
#         logging.error(f"Error rewriting bullets: {str(e)}")
#         return []

from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import torch
from dotenv import load_dotenv
import os
import logging
import time
import re

# Configure logging
logging.basicConfig(filename="app.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

load_dotenv()

# Use a better model if available, fallback to distilgpt2
try:
    model_name = "gpt2-medium"  # Better than distilgpt2 but still lightweight
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    logging.info(f"Successfully loaded {model_name}")
except Exception as e:
    logging.warning(f"Failed to load {model_name}, falling back to distilgpt2: {str(e)}")
    model_name = "distilgpt2"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)

# Create a text generation pipeline for easier use
try:
    generator = pipeline('text-generation', model=model, tokenizer=tokenizer, device=0 if torch.cuda.is_available() else -1)
    logging.info(f"Using GPU: {torch.cuda.is_available()}")
except Exception as e:
    logging.warning(f"Failed to create pipeline with GPU, using CPU: {str(e)}")
    generator = pipeline('text-generation', model=model, tokenizer=tokenizer)

def truncate_prompt(text, max_tokens=400):
    """Truncate text to fit within max_tokens."""
    try:
        tokens = tokenizer.encode(text, truncation=True, max_length=max_tokens)
        truncated_text = tokenizer.decode(tokens, skip_special_tokens=True)
        logging.info(f"Truncated text to {len(tokens)} tokens")
        return truncated_text
    except Exception as e:
        logging.error(f"Error truncating prompt: {str(e)}")
        return text[:100]  # Fallback to character-based truncation

def extract_tips(text):
    """Extract improvement tips from generated text."""
    # Try to find numbered or bulleted tips
    tips = []
    
    # Look for numbered tips (1. Tip text)
    numbered_pattern = re.compile(r'\d+\.\s*(.*?)(?=\d+\.|$)', re.DOTALL)
    numbered_matches = numbered_pattern.findall(text)
    if numbered_matches:
        tips = [tip.strip() for tip in numbered_matches if tip.strip()]
    
    # If no numbered tips, look for bullet points
    if not tips:
        bullet_pattern = re.compile(r'[-•*]\s*(.*?)(?=[-•*]|$)', re.DOTALL)
        bullet_matches = bullet_pattern.findall(text)
        if bullet_matches:
            tips = [tip.strip() for tip in bullet_matches if tip.strip()]
    
    # If still no tips, split by newlines and take non-empty lines
    if not tips:
        tips = [line.strip() for line in text.split('\n') if line.strip() and len(line.strip()) > 10]
    
    return tips

def generate_improvement_tips(resume_sections, job_description, missing_skills):
    """Generate improvement tips for a resume based on job description and missing skills."""
    start_time = time.time()
    try:
        # Create a concise summary of the resume
        resume_summary = "Skills: " + ", ".join(resume_sections.get("skills", [])) + ". "
        
        if resume_sections.get("experience"):
            resume_summary += "Experience: " + " ".join(resume_sections.get("experience", [])[:2]) + ". "
        
        if resume_sections.get("education"):
            resume_summary += "Education: " + " ".join(resume_sections.get("education", [])[:1])
        
        # Truncate inputs to fit within token limits
        resume_text = truncate_prompt(resume_summary, max_tokens=150)
        job_text = truncate_prompt(job_description, max_tokens=150)
        skills_text = truncate_prompt(', '.join(missing_skills), max_tokens=50)

        # Create a more detailed prompt for better results
        prompt = f"""
        You are an expert resume writer helping a job seeker improve their resume for a specific job.
        
        Resume summary: {resume_text}
        
        Job description: {job_text}
        
        Skills missing from the resume: {skills_text}
        
        Provide 5 specific, actionable tips to improve the resume and make it more competitive for this job. 
        Each tip should be concise and directly address how to better align the resume with the job requirements.
        
        Format as numbered tips:
        1. [First improvement tip]
        2. [Second improvement tip]
        3. [Third improvement tip]
        4. [Fourth improvement tip]
        5. [Fifth improvement tip]
        """
        
        # Ensure prompt fits within token limits
        prompt = truncate_prompt(prompt, max_tokens=400)
        logging.info(f"Improvement tips prompt token count: {len(tokenizer.encode(prompt))}")

        # Generate text with improved parameters
        outputs = generator(
            prompt,
            max_new_tokens=200,
            num_return_sequences=1,
            temperature=0.7,
            top_p=0.9,
            do_sample=True,
            no_repeat_ngram_size=2
        )
        
        # Extract the generated text
        response = outputs[0]['generated_text'][len(prompt):].strip()
        logging.info(f"Generated improvement tips in {time.time() - start_time:.2f} seconds")
        
        # Extract tips from the response
        tips = extract_tips(response)
        
        # Ensure we have at least 5 tips
        if len(tips) < 5:
            # Add fallback tips based on missing skills or job description
            fallback_tips = [
                f"Add {missing_skills[0] if missing_skills else 'relevant skills'} to your skills section to address the job requirements.",
                "Quantify your achievements with specific metrics and results to demonstrate impact.",
                "Tailor your resume summary to highlight experience relevant to this specific role.",
                "Use action verbs at the beginning of each bullet point to make your experience more impactful.",
                "Ensure your resume is ATS-friendly by using standard section headings and incorporating keywords from the job description."
            ]
            
            # Add fallback tips until we have 5
            tips.extend(fallback_tips[:(5-len(tips))])
        
        # Return only the first 5 tips
        return tips[:5]
    
    except Exception as e:
        logging.error(f"Error generating improvement tips: {str(e)}")
        # Provide more tailored fallback tips
        return [
            f"Add {missing_skills[0] if missing_skills else 'relevant skills'} to your skills section to address the job requirements.",
            "Quantify your achievements with specific metrics and results to demonstrate impact.",
            "Tailor your resume summary to highlight experience relevant to this specific role.",
            "Use action verbs at the beginning of each bullet point to make your experience more impactful.",
            "Ensure your resume is ATS-friendly by using standard section headings and incorporating keywords from the job description."
        ]

def rewrite_bullet_points(resume_sections):
    """Rewrite weak bullet points to be more impactful."""
    try:
        # Identify weak bullet points
        weak_bullets = []
        if resume_sections.get("experience"):
            for bullet in resume_sections.get("experience", []):
                # Check for indicators of weak bullets
                if (len(bullet.split()) < 10 or 
                    not any(word in bullet.lower() for word in ["increased", "decreased", "improved", "developed", "created", "managed", "led"]) or
                    "responsible for" in bullet.lower()):
                    weak_bullets.append(bullet)
        
        if not weak_bullets:
            return []
        
        rewritten = []
        for bullet in weak_bullets[:3]:  # Limit to 3 bullets to avoid token issues
            prompt = f"""
            Rewrite this resume bullet point to be more impactful by adding specific achievements, metrics, and using strong action verbs:
            
            Original: {bullet}
            
            Improved version:
            """
            
            prompt = truncate_prompt(prompt, max_tokens=150)
            
            # Generate improved bullet point
            outputs = generator(
                prompt,
                max_new_tokens=100,
                num_return_sequences=1,
                temperature=0.7,
                top_p=0.9,
                do_sample=True
            )
            
            # Extract the generated text
            response = outputs[0]['generated_text'][len(prompt):].strip()
            
            # Clean up the response
            improved_bullet = response.replace("Improved version:", "").strip()
            if improved_bullet:
                rewritten.append(improved_bullet)
        
        return rewritten
    
    except Exception as e:
        logging.error(f"Error rewriting bullets: {str(e)}")
        return []