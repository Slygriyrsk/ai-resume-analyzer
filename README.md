# 🧠 AI-Powered Resume Analyzer 📝

![Logo](https://raw.githubusercontent.com/Slygriyrsk/ai-resume-analyzer/main/static/logo.png)

**Supercharge your job search with AI-driven resume insights and optimization.**

---

## 🚩 Project Badges

[![🌟 Stars](https://img.shields.io/github/stars/Slygriyrsk/ai-resume-analyzer?style=flat-square&color=ff69b4&label=Stars)](https://github.com/Slygriyrsk/ai-resume-analyzer/stargazers)
[![🍴 Forks](https://img.shields.io/github/forks/Slygriyrsk/ai-resume-analyzer?style=flat-square&color=orange&label=Forks)](https://github.com/Slygriyrsk/ai-resume-analyzer/network)
[![🐛 Issues](https://img.shields.io/github/issues/Slygriyrsk/ai-resume-analyzer?style=flat-square&color=yellow&label=Issues)](https://github.com/Slygriyrsk/ai-resume-analyzer/issues)
[![📜 License](https://img.shields.io/github/license/Slygriyrsk/ai-resume-analyzer?style=flat-square&color=lightblue&label=License)](https://github.com/Slygriyrsk/ai-resume-analyzer/blob/main/LICENSE)
[![🛠️ Maintained](https://img.shields.io/badge/Maintained-Yes-success?style=flat-square)](https://github.com/Slygriyrsk/ai-resume-analyzer/graphs/commit-activity)
[![❤️ Made with Love](https://img.shields.io/badge/Made%20With-%F0%9F%92%95-pink?style=flat-square)](https://github.com/Slygriyrsk)

---

## ⚙️ Tech Stack

[![🐍 Python](https://img.shields.io/badge/Python-3.9_|_3.10_|_3.11-blue?style=flat-square&logo=python)](https://www.python.org/)
[![⚡ FastAPI](https://img.shields.io/badge/FastAPI-0.103.0-009688?style=flat-square&logo=fastapi)](https://fastapi.tiangolo.com/)
[![📊 Streamlit](https://img.shields.io/badge/Streamlit-1.27.0-FF4B4B?style=flat-square&logo=streamlit)](https://streamlit.io/)
[![🤗 HuggingFace](https://img.shields.io/badge/HuggingFace-Transformers-yellow?style=flat-square&logo=huggingface)](https://huggingface.co/)

---

## 🔗 Useful Links

- [🚀 Live Demo](https://Slygriyrsk.github.io/ai-resume-analyzer)
- [🐛 Report a Bug](https://github.com/Slygriyrsk/ai-resume-analyzer/issues)
- [✨ Request a Feature](https://github.com/Slygriyrsk/ai-resume-analyzer/issues)
- [📚 Documentation](https://github.com/Slygriyrsk/ai-resume-analyzer/wiki)


## ✨ Welcome to the AI-Powered Resume Analyzer! 

🚀 This web application helps job seekers optimize their resumes by analyzing them against job descriptions, providing ATS (Applicant Tracking System) scores, match scores, missing skills, improvement tips, and mock interview questions. Built with FastAPI (backend), Streamlit (frontend), and advanced NLP models, it's a powerful tool for career advancement. 🎯

This README provides a detailed guide to the project, including setup, folder structure, dependencies, errors faced, current functionality, limitations, and futuristic enhancements. Whether you're a developer contributing to the project or a user optimizing your resume, this document has you covered! 😊

---

## 📋 Table of Contents

- [Project Overview](#-project-overview)
- [Features](#-features)
- [Demo](#-demo)
- [Folder Structure](#-folder-structure)
- [Requirements](#-requirements)
- [Installation](#-installation)
- [Errors Faced During Installation](#-errors-faced-during-installation)
- [How the Current Model Works](#-how-the-current-model-works)
- [Current Issues](#-current-issues)
- [Futuristic Enhancements](#-futuristic-enhancements)
- [Testing](#-testing)
- [Usage](#-usage)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [Contact](#-contact)
- [Acknowledgments](#-acknowledgments)

---

## 🌟 Project Overview

The AI-Powered Resume Analyzer is a full-stack web application designed to:

📄 **Parse Resumes**: Extract skills, experience, and education from PDF/DOCX resumes.

🔍 **Analyze Fit**: Compare resumes to job descriptions using NLP and machine learning.

📊 **Score Resumes**: Provide ATS and match scores to gauge job fit.

💡 **Offer Insights**: Suggest missing skills and improvement tips.

🎤 **Prepare for Interviews**: Generate mock interview questions with sample answers.

✍️ **Collect Feedback**: Allow users to submit feedback for continuous improvement.

The application uses FastAPI for a robust API, Streamlit for an interactive UI with visualizations (e.g., ATS score gauge, match score bar, missing skills word cloud), and models like all-MiniLM-L6-v2 and distilgpt2 for NLP tasks. It's designed to be user-friendly, scalable, and extensible. 🌐

---

## 🚀 Features

- ⚡ **Real-time Analysis**: Get instant feedback on your resume
- 📊 **Interactive Visualizations**: Understand your resume's strengths and weaknesses
- 🤖 **AI-Powered Matching**: Advanced NLP models compare your resume to job descriptions
- 📈 **ATS Optimization**: Improve your resume's chances with Applicant Tracking Systems
- 🎯 **Skill Gap Analysis**: Identify missing skills for your target job
- 💬 **Interview Preparation**: Generate custom interview questions and sample answers
- 📱 **Responsive Design**: Use on desktop or mobile devices
- 🔒 **Privacy-Focused**: Your data stays on your device

---

## 🎬 Demo

[![Demo Video](https://img.shields.io/badge/Watch-Demo%20Video-red?style=for-the-badge&logo=youtube)](https://youtube.com/yourusername)

---

## 📂 Folder Structure

Here's the project's folder structure, located at C:\Users\sahar\OneDrive\Documents\AI\resume_analyzer:

```
📂 ai-resume-analyzer/
├── 📂 data/                          # Sample data for testing
│   ├── 📄 sample_resume.pdf          # Sample resume (PDF)
│   └── 📄 sample_job.txt             # Sample job description
├── 📂 static/                        # Static files (CSS)
│   └── 📄 styles.css                 # Custom CSS for Streamlit
├── 📂 venv/                          # Virtual environment
├── 📄 .env                           # Environment variables (PostgreSQL config)
├── 📄 app.py                         # Streamlit frontend (UI)
├── 📄 main.py                        # FastAPI backend (API)
├── 📄 matcher.py                     # Matches resume to job description
├── 📄 interview_prep.py              # Generates mock interview questions
├── 📄 resume_parser.py               # Parses resume (PDF/DOCX) [Pending]
├── 📄 ats_scorer.py                  # Calculates ATS score [Pending]
├── 📄 improvement_tips.py            # Suggests resume improvements
├── 📄 learning_paths.py              # Suggests learning paths [Optional]
├── 📄 generate_synthetic_data.py     # Generates synthetic data for training
├── 📄 train_ats_model.py             # Trains ATS scoring model
├── 📄 test.py                        # Unit tests
├── 📄 requirements.txt               # Python dependencies
├── 📄 feedback.txt                   # User feedback
├── 📄 app.log                        # Application logs
└── 📄 README.md                      # This file
```

### 📁 Key Folders and Files

- **data/**: Stores sample resumes and job descriptions for testing.
- **static/**: Contains styles.css for UI styling.
- **venv/**: Virtual environment for dependency isolation.
- **.env**: Stores PostgreSQL credentials (e.g., POSTGRES_HOST=localhost).
- **app.py**: Streamlit frontend with visualizations (ATS gauge, match bar, word cloud).
- **main.py**: FastAPI backend with /analyze endpoint.
- **matcher.py**: Uses all-MiniLM-L6-v2 to compute match scores and missing skills.
- **interview_prep.py**: Uses distilgpt2 to generate interview questions.
- **resume_parser.py**: Extracts resume sections (skills, experience, education) [Pending].
- **ats_scorer.py**: Computes ATS scores [Pending].
- **requirements.txt**: Lists all Python dependencies.
- **app.log**: Logs application events and errors.

---

## 🛠️ Requirements

[![Python](https://img.shields.io/badge/Python-3.9_|_3.10_|_3.11-yellow?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![PostgreSQL (Optional)](https://img.shields.io/badge/PostgreSQL-Optional-316192?style=flat-square&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![OS: Windows](https://img.shields.io/badge/OS-Windows_10/11-0078D6?style=flat-square&logo=windows&logoColor=white)](https://www.microsoft.com/windows)
[![CPU](https://img.shields.io/badge/CPU-4+_Cores-orange?style=flat-square&logo=intel&logoColor=white)](https://www.intel.com/)
[![RAM](https://img.shields.io/badge/RAM-8GB+_Recommended-FF69B4?style=flat-square&logo=databricks&logoColor=white)](https://www.crucial.com/)
[![Disk](https://img.shields.io/badge/Disk-5GB+_Free-success?style=flat-square&logo=vercel&logoColor=white)](https://www.samsung.com/semiconductor/minisite/ssd/)


To run the project, you need:

- **Operating System**: Windows 10/11 (tested on Windows).
- **Python**: Version 3.9--3.11.
- **PostgreSQL**: Optional (if used for resume storage).
- **Hardware**:
  - CPU: 4+ cores recommended.
  - RAM: 8GB+ (16GB for model inference).
  - Disk: ~5GB for dependencies and models.

### 📦 Dependencies

Listed in requirements.txt:

```
fastapi==0.103.0
uvicorn==0.23.2
pdfplumber==0.10.2
python-docx==0.8.11
spacy==3.7.2
sentence-transformers==2.2.2
streamlit==1.27.0
scikit-learn==1.3.0
xgboost==2.0.3
requests==2.31.0
psycopg2-binary==2.9.9
python-dotenv==1.0.0
numpy==1.26.0
pandas==2.1.0
transformers==4.30.2
torch==2.0.1
huggingface_hub==0.23.4
nltk==3.8.1
python-multipart==0.0.9
plotly==5.18.0
wordcloud==1.9.3
matplotlib==3.8.4
```

### 🔍 Key Dependencies

- **fastapi**: Powers the backend API.
- **streamlit**: Creates the interactive frontend.
- **sentence-transformers**: Provides all-MiniLM-L6-v2 for embedding resumes and job descriptions.
- **transformers**: Uses distilgpt2 for interview question generation.
- **pdfplumber**: Parses PDF resumes.
- **python-multipart**: Handles file uploads in FastAPI.
- **plotly, wordcloud, matplotlib**: Enable UI visualizations.

---

## 🚀 Installation

Follow these steps to set up the project on Windows.

### 1. Clone the Repository

```shellscript
git clone https://github.com/Slygriyrsk/ai-resume-analyzer.git
cd ai-resume-analyzer
```

### 2. Create and Activate Virtual Environment

Isolate dependencies:

```shellscript
python -m venv venv
source venv/Scripts/activate
```

### 3. Install Dependencies

Install required packages:

```shellscript
pip install -r requirements.txt
```

Download additional NLP resources:

```shellscript

python -m nltk.downloader punkt
python -m spacy download en_core_web_sm

```

### 4. Configure Environment Variables

Create a .env file in the root directory:

```plaintext

POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=resume_analyzer
POSTGRES_USER=your_username
POSTGRES_PASSWORD=your_password

```

Note: PostgreSQL is optional. If not used, remove psycopg2-binary from requirements.txt.

### 5. Create Sample Data

Create sample files for testing:

**data/sample_resume.pdf**:

Content:
```plaintext
Skills: Python, MongoDB, Git
Experience: Developed a web app using Flask
Education: BTech in ECE, 9.14/10, 2022--2026
```

**data/sample_job.txt**:

```shellscript
echo Software Engineer role requiring Python, AWS, Docker. > data\sample_job.txt
```

### 6. Generate Synthetic Data

Run scripts to create training data and train the ATS model:

```shellscript
python generate_synthetic_data.py
python train_ats_model.py
```

### 7. Run the Application

Start the FastAPI backend:

```shellscript
set HF_HUB_DISABLE_SYMLINKS_WARNING=1
python -m uvicorn main:app --host 0.0.0.0 --port 8000
```

Start the Streamlit frontend:

```shellscript
streamlit run app.py
```

### 8. Access the Application

Open [http://localhost:8501](http://localhost:8501) in your browser to:

- Upload a resume (PDF/DOCX).
- Paste a job description.
- View analysis results (ATS score, match score, missing skills, tips, interview questions).
- Submit feedback.

## 🐛 Errors Faced During Installation

Here are the errors we encountered, their causes, and solutions:

| **Error**                         | **Cause**                                                                                      | **Solution**                                                                                           |
|----------------------------------|------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| **Dependency Conflict**          | Version conflicts between FastAPI, Streamlit, and Transformers.                               | - Pin versions (e.g., `fastapi==0.103.0`, `transformers==4.30.2`)<br>- Update `requirements.txt`.      |
| **ImportError**                  | Missing modules during runtime.                                                               | - Add missing dependencies (e.g., `python-multipart`)<br>- Run `pip install -r requirements.txt`.      |
| **IndexError in Prompt Truncation** | Token counts exceeded model limits.                                                           | - Implement `truncate_prompt` to limit tokens to 300.                                                  |
| **Python-Multipart Error**       | `Form data requires "python-multipart" to be installed.`<br>Module required for FastAPI forms. | - Add `python-multipart==0.0.9` to `requirements.txt`<br>- Install via `pip install python-multipart`. |
| **PDF Parsing Issues**           | Malformed resume sections (e.g., "response", "seamlessdatahandling.").                         | - Pending (requires `resume_parser.py`).                                                               |
| **Low ATS Score (10.02%)**       | Poor parsing and strict scoring in `ats_scorer.py`.                                           | - Pending (requires `ats_scorer.py`).                                                                  |


## 🔍 How the Current Model Works

The application integrates multiple components to analyze resumes:

### 1. Backend (FastAPI - main.py)

- **Endpoint**: `/analyze`

- **Functionality**:

- Accepts resume (PDF/DOCX) and job description (text).

- Calls resume_parser.py to extract sections.

- Uses matcher.py for match score and missing skills.

- Uses ats_scorer.py for ATS score.

- Uses improvement_tips.py and interview_prep.py for suggestions and questions.

- **Tech**:

- FastAPI: Handles API requests.

- python-multipart: Processes file uploads.

- psycopg2-binary: Optional database integration.

### 2. Frontend (Streamlit - app.py)

- **UI**:

- Tabs: "Analyze Resume" and "Feedback".

- Upload resume, input job description, display results.

- **Visualizations**:

- ATS Score Gauge: Color-coded (Plotly).

- Match Score Bar: Compares to 75% target.

- Missing Skills Word Cloud: Highlights gaps.

- **Tech**:

- Streamlit: Interactive UI.

- Plotly, WordCloud, Matplotlib: Visualizations.

- CSS: Custom styling (static/styles.css).

### 3. Resume Parsing (resume_parser.py)

- **Functionality**: Extracts skills, experience, education from resumes.

- **Issue**: Malformed outputs (e.g., "response", � characters).

- **Tech**: pdfplumber, python-docx.

### 4. Matching (matcher.py)

- **Functionality**:

- Uses all-MiniLM-L6-v2 to compute embeddings for resume and job description.

- Calculates cosine similarity for match score (~0.18--0.19 currently).

- Extracts keywords using spacy and a predefined SKILL_LIST.

- **Issue**: Generic keywords (software, engineer) inflate missing_skills.

- **Tech**: sentence-transformers, spacy.

### 5. ATS Scoring (ats_scorer.py)

- **Functionality**: Scores resume for ATS compatibility (currently 10.02%).

- **Issue**: Strict keyword matching; needs semantic analysis.

- **Tech**: Likely xgboost (pending file).

### 6. Improvement Tips (improvement_tips.py)

- **Functionality**: Suggests resume enhancements (e.g., add keywords).

- **Tech**: distilgpt2 with truncation.

### 7. Interview Prep (interview_prep.py)

- **Functionality**: Generates 3 mock questions with answers.

- **Issue**: Outputs placeholders ([Question], [Answer]).

- **Tech**: distilgpt2.

### 8. Logging (app.log)

- Tracks events (e.g., embedding generation, errors).

- Example:

```plaintext
2025-04-29 17:33:58,288 - INFO - Match result: {'match_score': 0.1838252693414688, 'missing_skills': ['software', 'engineer', 'role', 'python', 'aws', 'docker']}
```

## ⚠️ Current Issues

Despite progress, the application has limitations:

| **Issue**                      | **Impact**                                         | **Solution**                                                                 |
|-------------------------------|----------------------------------------------------|------------------------------------------------------------------------------|
| **Malformed Resume Parsing**  | Low ATS score (10.02%), inaccurate missing_skills. | Share `resume_parser.py` to clean outputs.                                  |
| **Low ATS Score**             | Misrepresents resume quality.                      | Share `ats_scorer.py` for semantic scoring.                                 |
| **Inaccurate Missing Skills** | Misguides users.                                   | Enhance `matcher.py` with `SKILL_LIST`; further refine with a better list.  |
| **Poor Interview Prep**       | Reduces usefulness.                                | Improve prompts/fallbacks; consider using a larger model.                   |
| **UI Limitations**            | Less engaging for users.                           | Add gauge, bar, word cloud; plan for interactive dashboards.                |
| **Performance**               | Longer analysis times.                             | Enable GPU support or optimize the model.                                   |

## 🚀 Futuristic Enhancements

To make the application cutting-edge, consider these enhancements:

### Advanced NLP Models ✨

- Replace all-MiniLM-L6-v2 with all-roberta-large-v1 for better embeddings.

- Use flan-t5-base instead of distilgpt2 for interview prep.

- **Benefit**: Improved semantic understanding, higher accuracy.

### Resume Parsing Improvements 📄

- Use OCR (e.g., pytesseract) for scanned PDFs.

- Implement custom NLP to extract structured sections.

- **Benefit**: Cleaner outputs, higher scores.

### Semantic ATS Scoring 🔍

- Train ats_scorer.py on real ATS data with BERT-based models.

- Use fuzzy matching for keywords.

- **Benefit**: Realistic ATS scores (e.g., 70--90% for good resumes).

### Interactive UI Dashboards 📊

- Add:

- Skill gap radar chart.

- Resume keyword density heatmap.

- Interview question difficulty slider.

- Use Dash or Plotly Dash for dynamic UI.

- **Benefit**: Engaging, professional interface.

### Database Integration 🗄️

- Store resumes and analyses in PostgreSQL.

- Enable user accounts for history tracking.

- **Benefit**: Personalized experience, scalability.

### Real-Time Job Scraping 🌐

- Integrate web scraping (e.g., beautifulsoup4) to fetch job descriptions from LinkedIn/Indeed.

- **Benefit**: Users can analyze against live postings.

### Learning Path Integration 📚

- Enhance learning_paths.py with APIs (e.g., Coursera, Udemy).

- Suggest courses for missing skills (e.g., AWS certification).

- **Benefit**: Actionable career growth.

### Multilingual Support 🌍

- Add language detection (langdetect) and translation (googletrans).

- Support non-English resumes/job descriptions.

- **Benefit**: Global accessibility.

### AI-Powered Resume Writing ✍️

- Use LLMs (e.g., Grok 3 via xAI API) to rewrite resume bullets.

- **Benefit**: Polished, ATS-friendly resumes.

### Cloud Deployment ☁️

- Deploy on AWS/GCP with Docker containers.

- Use Kubernetes for scalability.

- **Benefit**: High availability, global access.

### Mobile App 📱

- Develop iOS/Android app using Flutter/React Native.

- Integrate with Grok 3's voice mode (iOS-only).

- **Benefit**: Wider user base.

### Explainable AI 🧠

- Add explanations for ATS/match scores (e.g., "Low score due to missing 'AWS'").

- **Benefit**: User trust and transparency.


## 🧪 Testing

Run unit tests to verify functionality:

```python
import requests
import os

def test_resume_analyzer(resume_path, job_path):
    with open(resume_path, "rb") as f_resume, open(job_path, "r") as f_job:
        files = {"file": f_resume}
        data = {"text": f_job.read()}
        response = requests.post("http://localhost:8000/analyze", files=files, data=data)
        assert response.status_code == 200, f"Failed: {response.json()}"
        result = response.json()
        assert "ats_score" in result, "ATS score missing"
        print(f"Test passed for {resume_path}")
test_resume_analyzer("data/sample_resume.pdf", "data/sample_job.txt")
```

Run:

```shellscript
python test.py
```
## 📜 Usage

### Analyze Resume:

1\. Open [http://localhost:8501](http://localhost:8501).

2\. Upload a PDF/DOCX resume.

3\. Paste a job description (e.g., "Software Engineer role requiring Python, AWS, Docker").

4\. Click "Analyze Resume".

5\. View:

1\. ATS Score Gauge (0-100%).

2\. Match Score Bar (vs. 75% target).

3\. Missing Skills Word Cloud.

4\. Improvement Tips.

5\. Interview Questions.

### Submit Feedback:

1\. Go to the "Feedback" tab.

2\. Enter feedback.

3\. Submit to save in feedback.txt.

## 🛠️ Troubleshooting

### Python-Multipart Error:

```shellscript
pip install python-multipart==0.0.9
```

### Low ATS Score:

- Share resume_parser.py, ats_scorer.py.
- Test with a clean resume PDF.

### Interview Prep Issues:

Check app.log:

```shellscript
type app.log
```

### UI Issues:

Verify plotly, wordcloud, matplotlib:

```shellscript
pip show plotly wordcloud matplotlib
```

## 🤝 Contributing

Want to improve the project? 🙌

1\. Fork the repo (if on GitHub).

2\. Create a branch: `git checkout -b feature/your-feature`.

3\. Commit changes: `git commit -m "Add feature"`.

4\. Push: `git push origin feature/your-feature`.

5\. Open a pull request.

## 📧 Contact

For questions, contact:

- Email: [your.email@example.com](mailto:your.email@example.com)

- GitHub: github.com/your-username

## 🎉 Acknowledgments

- xAI: For inspiring AI-driven solutions.

- Streamlit & FastAPI: For amazing frameworks.

- Hugging Face: For sentence-transformers and transformers.
