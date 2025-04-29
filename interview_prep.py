# from transformers import AutoModelForCausalLM, AutoTokenizer
# import torch
# from dotenv import load_dotenv
# import os

# load_dotenv()

# # Load local LLM
# model_name = "distilbert/distilgpt2"
# tokenizer = AutoTokenizer.from_pretrained(model_name)
# model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16, device_map="auto")

# def generate_interview_prep(resume_sections, job_description, missing_skills):
#     prompt = f"""
#     Given the resume: {resume_sections}
#     And the job description: {job_description}
#     With missing skills: {', '.join(missing_skills)}
#     Generate 3 mock interview questions tailored to the job and resume gaps.
#     For each question, provide a sample answer that the candidate can use to prepare.
#     Format as:
#     Question: [Question]
#     Sample Answer: [Answer]
#     """
    
#     inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
#     outputs = model.generate(
#         **inputs,
#         max_length=1000,
#         num_return_sequences=1,
#         temperature=0.7,
#         do_sample=True
#     )
#     response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
#     # Parse response
#     questions = []
#     blocks = response.split("\n\n")[:3]
#     for block in blocks:
#         if "Question:" in block and "Sample Answer:" in block:
#             question = block.split("Question:")[1].split("Sample Answer:")[0].strip()
#             answer = block.split("Sample Answer:")[1].strip()
#             questions.append({"question": question, "sample_answer": answer})
    
#     return questions

# from transformers import AutoModelForCausalLM, AutoTokenizer
# import torch
# from dotenv import load_dotenv
# import os

# load_dotenv()

# # Load local LLM
# model_name = "distilbert/distilgpt2"
# tokenizer = AutoTokenizer.from_pretrained(model_name)
# model = AutoModelForCausalLM.from_pretrained(model_name)  # Removed torch_dtype and device_map

# def generate_interview_prep(resume_sections, job_description, missing_skills):
#     if missing_skills is None:
#         missing_skills = []
    
#     prompt = f"""
#     Given the resume: {resume_sections}
#     And the job description: {job_description}
#     With missing skills: {', '.join(missing_skills)}
#     Generate 3 mock interview questions tailored to the job and resume gaps.
#     For each question, provide a sample answer that the candidate can use to prepare.
#     Format as:
#     Question: [Question]
#     Sample Answer: [Answer]
#     """
    
#     inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=1024)
    
#     outputs = model.generate(
#         **inputs,
#         max_new_tokens=500,
#         num_return_sequences=1,
#         temperature=0.7,
#         do_sample=True
#     )
#     response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
#     # Parse response
#     questions = []
#     blocks = response.split("\n\n")[:3]
#     for block in blocks:
#         if "Question:" in block and "Sample Answer:" in block:
#             question = block.split("Question:")[1].split("Sample Answer:")[0].strip()
#             answer = block.split("Sample Answer:")[1].strip()
#             questions.append({"question": question, "sample_answer": answer})
    
#     return questions

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
#         return text[:100]

# def generate_interview_prep(resume_sections, job_description, missing_skills):
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
#         Generate 3 concise interview questions with sample answers.
#         Format:
#         Q: [Question]
#         A: [Answer]
#         """
        
#         # Ensure prompt fits within 400 tokens
#         prompt = truncate_prompt(prompt, max_tokens=400)
#         logging.info(f"Final prompt token count: {len(tokenizer.encode(prompt))}")

#         inputs = tokenizer(prompt, return_tensors="pt")
#         outputs = model.generate(
#             **inputs,
#             max_new_tokens=150,
#             num_return_sequences=1,
#             temperature=0.7,
#             do_sample=True
#         )
#         response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
#         # Parse response
#         questions = []
#         blocks = response.split("\n\n")[:3]
#         for block in blocks:
#             if "Q:" in block and "A:" in block:
#                 question = block.split("Q:")[1].split("A:")[0].strip()
#                 answer = block.split("A:")[1].strip()
#                 questions.append({"question": question, "sample_answer": answer})
        
#         return questions
#     except Exception as e:
#         logging.error(f"Error generating interview prep: {str(e)}")
#         return [
#             {"question": "Tell me about your experience.", "sample_answer": "Discuss relevant projects."},
#             {"question": "How do you handle challenges?", "sample_answer": "Describe a problem-solving experience."},
#             {"question": "Why this role?", "sample_answer": "Align your skills with the job."}
#         ]

# from transformers import AutoModelForCausalLM, AutoTokenizer
# import torch
# from dotenv import load_dotenv
# import os
# import logging

# # Configure logging
# logging.basicConfig(filename="app.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# load_dotenv()

# model_name = "distilbert/distilgpt2"
# tokenizer = AutoTokenizer.from_pretrained(model_name)
# model = AutoModelForCausalLM.from_pretrained(model_name)

# def truncate_prompt(text, max_tokens=300):
#     try:
#         tokens = tokenizer.encode(text, truncation=True, max_length=max_tokens)
#         truncated_text = tokenizer.decode(tokens, skip_special_tokens=True)
#         logging.info(f"Truncated text to {len(tokens)} tokens")
#         return truncated_text
#     except Exception as e:
#         logging.error(f"Error truncating prompt: {str(e)}")
#         return text[:100]

# def generate_interview_prep(resume_sections, job_description, missing_skills):
#     try:
#         resume_summary = "Skills: " + ", ".join(resume_sections.get("skills", [])[:3]) + ". "
#         resume_summary += "Experience: " + " ".join(resume_sections.get("experience", [])[:2]) + ". "
#         resume_summary += "Education: " + " ".join(resume_sections.get("education", [])[:1])
        
#         resume_text = truncate_prompt(resume_summary, max_tokens=100)
#         job_text = truncate_prompt(job_description, max_tokens=100)
#         skills_text = truncate_prompt(', '.join(missing_skills), max_tokens=50)

#         prompt = f"""
#         You are a career coach. Based on the following resume and job description, generate 3 specific interview questions with detailed sample answers to help the candidate prepare. Focus on technical skills and the job requirements. Format each as:
#         Q: [Specific question]
#         A: [Detailed answer]

#         Resume: {resume_text}
#         Job: {job_text}
#         Missing Skills: {skills_text}
#         """
        
#         prompt = truncate_prompt(prompt, max_tokens=300)
#         logging.info(f"Final prompt token count: {len(tokenizer.encode(prompt))}")

#         inputs = tokenizer(prompt, return_tensors="pt")
#         outputs = model.generate(
#             **inputs,
#             max_new_tokens=150,
#             num_return_sequences=1,
#             temperature=0.7,
#             do_sample=True
#         )
#         response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
#         questions = []
#         blocks = response.split("\n\n")[:3]
#         for block in blocks:
#             if "Q:" in block and "A:" in block:
#                 question = block.split("Q:")[1].split("A:")[0].strip()
#                 answer = block.split("A:")[1].strip()
#                 questions.append({"question": question, "sample_answer": answer})
        
#         # Fallback questions
#         while len(questions) < 3:
#             questions.append({
#                 "question": f"Describe your experience with {missing_skills[0] if missing_skills else 'Python'}.",
#                 "sample_answer": f"I have worked on projects using {missing_skills[0] if missing_skills else 'Python'}, such as developing a web app with Flask."
#             })
        
#         return questions
#     except Exception as e:
#         logging.error(f"Error generating interview prep: {str(e)}")
#         return [
#             {"question": "How have you used Python in projects?", "sample_answer": "I developed a web app using Python and Flask, implementing RESTful APIs."},
#             {"question": "Describe a challenging technical problem you solved.", "sample_answer": "I optimized a database query, reducing runtime by 40% using indexing."},
#             {"question": "Why are you a good fit for this role?", "sample_answer": "My skills in MongoDB and web development align with the job requirements."}
#         ]

from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import torch
from dotenv import load_dotenv
import os
import logging
import re
import time

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

def truncate_prompt(text, max_tokens=300):
    """Truncate text to fit within max_tokens."""
    try:
        tokens = tokenizer.encode(text, truncation=True, max_length=max_tokens)
        truncated_text = tokenizer.decode(tokens, skip_special_tokens=True)
        logging.info(f"Truncated text to {len(tokens)} tokens")
        return truncated_text
    except Exception as e:
        logging.error(f"Error truncating prompt: {str(e)}")
        return text[:100]  # Fallback to character-based truncation

def extract_qa_pairs(text):
    """Extract question-answer pairs from generated text."""
    qa_pairs = []
    
    # Try to find Q: and A: patterns
    qa_pattern = re.compile(r'Q:(.*?)A:(.*?)(?=Q:|$)', re.DOTALL)
    matches = qa_pattern.findall(text)
    
    if matches:
        for q, a in matches:
            qa_pairs.append({
                "question": q.strip(),
                "sample_answer": a.strip()
            })
    
    # If no matches found, try to split by newlines and create pairs
    if not qa_pairs:
        lines = [line.strip() for line in text.split('\n') if line.strip()]
        for i in range(0, len(lines)-1, 2):
            if i+1 < len(lines):
                qa_pairs.append({
                    "question": lines[i].replace("Question:", "").strip(),
                    "sample_answer": lines[i+1].replace("Answer:", "").strip()
                })
    
    return qa_pairs

def generate_interview_prep(resume_sections, job_description, missing_skills):
    """Generate interview questions and sample answers based on resume and job description."""
    start_time = time.time()
    try:
        # Create a concise summary of the resume
        resume_summary = "Skills: " + ", ".join(resume_sections.get("skills", [])[:5]) + ". "
        
        if resume_sections.get("experience"):
            resume_summary += "Experience: " + " ".join(resume_sections.get("experience", [])[:2]) + ". "
        
        if resume_sections.get("education"):
            resume_summary += "Education: " + " ".join(resume_sections.get("education", [])[:1])
        
        # Truncate inputs to fit within token limits
        resume_text = truncate_prompt(resume_summary, max_tokens=100)
        job_text = truncate_prompt(job_description, max_tokens=100)
        skills_text = truncate_prompt(', '.join(missing_skills), max_tokens=50)

        # Create a more detailed prompt for better results
        prompt = f"""
        You are an expert career coach helping a job candidate prepare for an interview.
        
        Resume summary: {resume_text}
        
        Job description: {job_text}
        
        Skills the candidate needs to develop: {skills_text}
        
        Generate 3 specific interview questions with detailed sample answers. Focus on technical skills, experience, and how the candidate can address their skill gaps.
        
        Format each as:
        Q: [Specific question related to the job or candidate's experience]
        A: [Detailed 3-4 sentence answer that demonstrates knowledge and experience]
        """
        
        # Ensure prompt fits within token limits
        prompt = truncate_prompt(prompt, max_tokens=300)
        logging.info(f"Interview prep prompt token count: {len(tokenizer.encode(prompt))}")

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
        logging.info(f"Generated interview prep in {time.time() - start_time:.2f} seconds")
        
        # Extract question-answer pairs
        questions = extract_qa_pairs(response)
        
        # Ensure we have at least 3 questions
        while len(questions) < 3:
            # Add fallback questions based on missing skills or job description
            skill = missing_skills[0] if missing_skills else "relevant experience"
            questions.append({
                "question": f"How would you address your lack of experience with {skill}?",
                "sample_answer": f"While I haven't directly worked with {skill}, I've developed similar skills through projects in {resume_sections.get('skills', ['related areas'])[0]}. I'm a quick learner and have already started online courses to build this competency. I believe my experience with {resume_sections.get('skills', ['transferable skills'])[0]} provides a strong foundation to quickly become proficient."
            })
        
        # Return only the first 3 questions
        return questions[:3]
    
    except Exception as e:
        logging.error(f"Error generating interview prep: {str(e)}")
        # Provide more tailored fallback questions
        return [
            {"question": "How does your experience align with this role?", 
             "sample_answer": "My experience in software development has equipped me with strong problem-solving skills and technical expertise that directly apply to this role. I've worked on similar projects that required the same technologies mentioned in the job description."},
            
            {"question": f"How would you address your lack of experience with {missing_skills[0] if missing_skills else 'a specific technology'}?", 
             "sample_answer": f"While I haven't worked extensively with {missing_skills[0] if missing_skills else 'that specific technology'}, I've used similar tools and am a quick learner. I've already started learning through online courses and personal projects to build this skill."},
            
            {"question": "Describe a challenging project you worked on and how you overcame obstacles.", 
             "sample_answer": "I led a web application project with tight deadlines and changing requirements. By implementing agile methodologies, maintaining clear communication with stakeholders, and prioritizing features, we delivered the project on time with all critical functionality."}
        ]