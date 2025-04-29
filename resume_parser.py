import pdfplumber
from docx import Document
import spacy
import re
import os

nlp = spacy.load("en_core_web_sm")

def parse_pdf(file_path):
    try:
        with pdfplumber.open(file_path) as pdf:
            text = "".join(page.extract_text() or "" for page in pdf.pages)
        return text
    except Exception as e:
        raise ValueError(f"Error parsing PDF: {str(e)}")

def parse_docx(file_path):
    try:
        doc = Document(file_path)
        text = "\n".join(paragraph.text for paragraph in doc.paragraphs if paragraph.text.strip())
        return text
    except Exception as e:
        raise ValueError(f"Error parsing DOCX: {str(e)}")

def extract_sections(text):
    if not text.strip():
        raise ValueError("Empty resume text")
    
    doc = nlp(text)
    sections = {"skills": [], "experience": [], "education": []}
    
    # Rule-based section detection with fallback
    current_section = None
    lines = text.split("\n")
    for line in lines:
        line = line.strip().lower()
        if not line:
            continue
        if re.search(r"skills|technical skills|proficiencies", line):
            current_section = "skills"
        elif re.search(r"experience|work experience|employment", line):
            current_section = "experience"
        elif re.search(r"education|academic|qualifications", line):
            current_section = "education"
        elif current_section and line:
            sections[current_section].append(line)
    
    # Fallback: If no skills section, extract skills from entire text
    if not sections["skills"]:
        for ent in doc.ents:
            if ent.label_ in ["SKILL", "NORP"] or ent.text.lower() in ["python", "java", "aws", "sql"]:
                sections["skills"].append(ent.text)
    
    # Remove duplicates
    for key in sections:
        sections[key] = list(set(sections[key]))
    
    return sections

def parse_resume(file_path):
    if file_path.endswith(".pdf"):
        text = parse_pdf(file_path)
    elif file_path.endswith(".docx"):
        text = parse_docx(file_path)
    else:
        raise ValueError("Unsupported file format")
    
    # Clean up temporary file
    if os.path.exists(file_path):
        os.remove(file_path)
    
    return extract_sections(text)