# import streamlit as st
# import requests
# import os
# import logging
# from datetime import datetime

# # Configure logging
# logging.basicConfig(filename="streamlit.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# # Set page configuration
# st.set_page_config(page_title="AI-Powered Resume Analyzer", layout="wide", initial_sidebar_state="expanded")

# # Load custom CSS
# css_path = "static/styles.css"
# if os.path.exists(css_path):
#     with open(css_path) as f:
#         st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
# else:
#     st.markdown("""
#     <style>
#     body {
#         font-family: 'Arial', sans-serif;
#         background-color: #f0f2f6;
#     }
#     .main {
#         background-color: #ffffff;
#         padding: 20px;
#         border-radius: 10px;
#         box-shadow: 0 4px 8px rgba(0,0,0,0.1);
#     }
#     .stButton>button {
#         background-color: #4CAF50;
#         color: white;
#         border-radius: 5px;
#         padding: 10px 20px;
#         border: none;
#         font-weight: bold;
#     }
#     .stFileUploader {
#         border: 2px dashed #4CAF50;
#         border-radius: 5px;
#         padding: 10px;
#         background-color: #f9f9f9;
#     }
#     .stTextArea textarea {
#         border: 1px solid #4CAF50;
#         border-radius: 5px;
#         padding: 10px;
#         font-size: 14px;
#     }
#     .metric {
#         background-color: #e8f4f8;
#         padding: 15px;
#         border-radius: 5px;
#         box-shadow: 0 2px 4px rgba(0,0,0,0.1);
#         margin: 10px 0;
#         text-align: center;
#     }
#     .stTabs [data-baseweb="tab"] {
#         font-size: 16px;
#         font-weight: bold;
#         color: #333;
#     }
#     .stTabs [data-baseweb="tab-highlight"] {
#         background-color: #4CAF50;
#     }
#     </style>
#     """, unsafe_allow_html=True)
#     logging.warning("Custom CSS file not found, using fallback CSS")

# @st.cache_data
# def analyze_resume(file, job_description):
#     try:
#         files = {"file": file}
#         data = {"text": job_description}
#         response = requests.post("http://localhost:8000/analyze", files=files, data=data)
#         response.raise_for_status()
#         return response.json()
#     except Exception as e:
#         logging.error(f"Error analyzing resume: {str(e)}")
#         st.error(f"Error analyzing resume: {str(e)}")
#         return None

# def save_feedback(feedback, rating):
#     try:
#         with open("feedback.txt", "a") as f:
#             timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#             f.write(f"[{timestamp}] Rating: {rating}/5\nFeedback: {feedback}\n\n")
#         logging.info("Feedback saved successfully")
#         st.success("Thank you for your feedback!")
#     except Exception as e:
#         logging.error(f"Error saving feedback: {str(e)}")
#         st.error(f"Error saving feedback: {str(e)}")

# def main():
#     st.title("AI-Powered Resume Analyzer")
#     st.markdown("Upload your resume and job description to get tailored insights and improvement tips.")

#     # Create tabs for different sections
#     tab1, tab2, tab3 = st.tabs(["Analyze Resume", "Feedback", "About"])

#     with tab1:
#         st.header("Resume Analysis")
#         col1, col2 = st.columns([1, 1])

#         with col1:
#             st.subheader("Upload Resume (PDF/DOCX)")
#             resume_file = st.file_uploader("Choose a file", type=["pdf", "docx"], key="resume")

#         with col2:
#             st.subheader("Job Description")
#             job_description = st.text_area("Paste job description here", height=150, key="job_desc")

#         if st.button("Analyze Resume", key="analyze"):
#             if resume_file and job_description:
#                 with st.spinner("Analyzing your resume..."):
#                     result = analyze_resume(resume_file, job_description)
#                     if result:
#                         st.session_state["analysis_result"] = result
#                         logging.info("Resume analysis completed successfully")
#             else:
#                 st.error("Please upload a resume and provide a job description.")
#                 logging.warning("Analysis attempted without resume or job description")

#         # Display results if available
#         if "analysis_result" in st.session_state:
#             result = st.session_state["analysis_result"]
#             st.subheader("Analysis Results")

#             # Metrics
#             col1, col2 = st.columns(2)
#             with col1:
#                 st.markdown(f"<div class='metric'><b>ATS Score</b><br>{result.get('ats_score', 0):.2f}%</div>", unsafe_allow_html=True)
#             with col2:
#                 st.markdown(f"<div class='metric'><b>Match Score</b><br>{result.get('match_score', 0):.2f}%</div>", unsafe_allow_html=True)

#             # Missing Skills
#             with st.expander("Missing Skills", expanded=True):
#                 missing_skills = result.get("missing_skills", [])
#                 if missing_skills:
#                     st.write("Skills to consider adding to your resume:")
#                     for skill in missing_skills:
#                         st.markdown(f"- {skill}")
#                 else:
#                     st.write("No critical skills missing!")

#             # Improvement Tips
#             with st.expander("Improvement Tips", expanded=True):
#                 tips = result.get("improvement_tips", [])
#                 if tips:
#                     st.write("Actionable suggestions to enhance your resume:")
#                     for tip in tips:
#                         st.markdown(f"- {tip}")
#                 else:
#                     st.write("No specific improvement tips available.")

#             # Interview Prep
#             with st.expander("Interview Preparation", expanded=True):
#                 questions = result.get("interview_questions", [])
#                 if questions:
#                     st.write("Mock interview questions and sample answers:")
#                     for q in questions:
#                         st.markdown(f"**Question:** {q['question']}")
#                         st.markdown(f"**Sample Answer:** {q['sample_answer']}")
#                 else:
#                     st.write("No interview questions generated.")

#     with tab2:
#         st.header("Feedback")
#         st.markdown("We value your input to improve the Resume Analyzer!")
#         with st.form(key="feedback_form"):
#             feedback = st.text_area("Your Feedback", height=100, placeholder="Share your thoughts or suggestions...")
#             rating = st.slider("Rate your experience", 1, 5, 3)
#             submit_feedback = st.form_submit_button("Submit Feedback")
#             if submit_feedback:
#                 if feedback:
#                     save_feedback(feedback, rating)
#                 else:
#                     st.error("Please provide feedback before submitting.")
#                     logging.warning("Feedback submission attempted without input")

#     with tab3:
#         st.header("About")
#         st.markdown("""
#         The AI-Powered Resume Analyzer uses advanced AI to analyze your resume against job descriptions.
#         Features include:
#         - **ATS Score**: Evaluates resume compatibility with Applicant Tracking Systems.
#         - **Match Score**: Measures alignment with job requirements.
#         - **Improvement Tips**: Provides actionable suggestions.
#         - **Interview Prep**: Generates tailored questions and answers.
#         Built with Streamlit, FastAPI, and Transformers.
#         """)

# if __name__ == "__main__":
#     main()

# import streamlit as st
# import requests
# import os
# import logging
# import pandas as pd
# import numpy as np
# import plotly.express as px
# import plotly.graph_objects as go
# import time
# from datetime import datetime
# import random
# import altair as alt

# # Configure logging
# logging.basicConfig(filename="streamlit.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# # Set page configuration
# st.set_page_config(
#     page_title="AI-Powered Resume Analyzer",
#     layout="wide",
#     initial_sidebar_state="expanded",
#     page_icon="📝"
# )

# # Load custom CSS
# css_path = "static/styles.css"
# if os.path.exists(css_path):
#     with open(css_path) as f:
#         st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
#     logging.info("Custom CSS loaded successfully")
# else:
#     logging.warning("Custom CSS file not found, using fallback CSS")
#     st.warning("Custom CSS file not found. Please create the file at 'static/styles.css' for the best experience.")

# # Cache function for resume analysis
# @st.cache_data
# def analyze_resume(file, job_description):
#     try:
#         files = {"file": file}
#         data = {"text": job_description}
#         response = requests.post("http://localhost:8000/analyze", files=files, data=data)
#         response.raise_for_status()
#         return response.json()
#     except Exception as e:
#         logging.error(f"Error analyzing resume: {str(e)}")
#         st.error(f"Error analyzing resume: {str(e)}")
#         return None

# # Function to save feedback
# def save_feedback(feedback, rating):
#     try:
#         with open("feedback.txt", "a") as f:
#             timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#             f.write(f"[{timestamp}] Rating: {rating}/5\nFeedback: {feedback}\n\n")
#         logging.info("Feedback saved successfully")
#         return True
#     except Exception as e:
#         logging.error(f"Error saving feedback: {str(e)}")
#         st.error(f"Error saving feedback: {str(e)}")
#         return False

# # Function to create a radar chart for skills
# def create_skills_radar_chart(resume_skills, job_skills):
#     # Create a set of all skills
#     all_skills = set(resume_skills + job_skills)
    
#     # Create data for the radar chart
#     categories = list(all_skills)
#     resume_values = [1 if skill in resume_skills else 0 for skill in categories]
#     job_values = [1 if skill in job_skills else 0 for skill in categories]
    
#     # Create the radar chart
#     fig = go.Figure()
    
#     fig.add_trace(go.Scatterpolar(
#         r=resume_values,
#         theta=categories,
#         fill='toself',
#         name='Your Resume',
#         line_color='#3b82f6',
#         fillcolor='rgba(59, 130, 246, 0.2)'
#     ))
    
#     fig.add_trace(go.Scatterpolar(
#         r=job_values,
#         theta=categories,
#         fill='toself',
#         name='Job Requirements',
#         line_color='#1e3a8a',
#         fillcolor='rgba(30, 58, 138, 0.2)'
#     ))
    
#     fig.update_layout(
#         polar=dict(
#             radialaxis=dict(
#                 visible=True,
#                 range=[0, 1]
#             )
#         ),
#         showlegend=True,
#         legend=dict(
#             orientation="h",
#             yanchor="bottom",
#             y=1.1,
#             xanchor="center",
#             x=0.5
#         ),
#         height=500,
#         margin=dict(l=80, r=80, t=20, b=20),
#         paper_bgcolor='rgba(0,0,0,0)',
#         plot_bgcolor='rgba(0,0,0,0)'
#     )
    
#     return fig

# # Function to create a score gauge chart
# def create_gauge_chart(score, title):
#     fig = go.Figure(go.Indicator(
#         mode="gauge+number",
#         value=score,
#         domain={'x': [0, 1], 'y': [0, 1]},
#         title={'text': title, 'font': {'size': 24, 'color': '#1e3a8a', 'family': 'Montserrat'}},
#         gauge={
#             'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "#1e3a8a"},
#             'bar': {'color': "#3b82f6"},
#             'bgcolor': "white",
#             'borderwidth': 2,
#             'bordercolor': "#1e3a8a",
#             'steps': [
#                 {'range': [0, 30], 'color': 'rgba(255, 99, 132, 0.3)'},
#                 {'range': [30, 70], 'color': 'rgba(255, 205, 86, 0.3)'},
#                 {'range': [70, 100], 'color': 'rgba(75, 192, 192, 0.3)'}
#             ],
#             'threshold': {
#                 'line': {'color': "red", 'width': 4},
#                 'thickness': 0.75,
#                 'value': 90
#             }
#         }
#     ))
    
#     fig.update_layout(
#         height=300,
#         margin=dict(l=20, r=20, t=50, b=20),
#         paper_bgcolor='rgba(0,0,0,0)',
#         font={'color': "#1e3a8a", 'family': "Montserrat"}
#     )
    
#     return fig

# # Function to create a bar chart for skill match
# def create_skill_match_chart(resume_skills, job_skills):
#     # Count the number of skills in each category
#     resume_count = len(resume_skills)
#     job_count = len(job_skills)
#     matched_count = len(set(resume_skills).intersection(set(job_skills)))
#     missing_count = job_count - matched_count
    
#     # Create data for the bar chart
#     categories = ['Resume Skills', 'Job Skills', 'Matched Skills', 'Missing Skills']
#     values = [resume_count, job_count, matched_count, missing_count]
#     colors = ['#3b82f6', '#1e3a8a', '#10b981', '#ef4444']
    
#     # Create the bar chart
#     fig = go.Figure(go.Bar(
#         x=categories,
#         y=values,
#         marker_color=colors,
#         text=values,
#         textposition='auto'
#     ))
    
#     fig.update_layout(
#         title={
#             'text': 'Skills Analysis',
#             'y':0.9,
#             'x':0.5,
#             'xanchor': 'center',
#             'yanchor': 'top',
#             'font': {'size': 20, 'color': '#1e3a8a', 'family': 'Montserrat'}
#         },
#         xaxis_title="Categories",
#         yaxis_title="Count",
#         height=400,
#         margin=dict(l=20, r=20, t=80, b=20),
#         paper_bgcolor='rgba(0,0,0,0)',
#         plot_bgcolor='rgba(0,0,0,0)',
#         font={'color': "#1e3a8a", 'family': "Montserrat"}
#     )
    
#     return fig

# # Function to simulate resume analysis for demo purposes
# def simulate_resume_analysis(job_description):
#     # Simulate processing time
#     progress_bar = st.progress(0)
#     status_text = st.empty()
    
#     for i in range(101):
#         # Update progress bar
#         progress_bar.progress(i)
        
#         # Update status text based on progress
#         if i < 20:
#             status_text.text("Extracting text from resume...")
#         elif i < 40:
#             status_text.text("Analyzing resume structure...")
#         elif i < 60:
#             status_text.text("Identifying skills and experience...")
#         elif i < 80:
#             status_text.text("Comparing with job description...")
#         else:
#             status_text.text("Finalizing analysis...")
        
#         time.sleep(0.05)
    
#     # Clear progress indicators
#     progress_bar.empty()
#     status_text.empty()
    
#     # Generate sample skills
#     all_skills = [
#         "python", "java", "javascript", "react", "node.js", "mongodb",
#         "sql", "aws", "docker", "kubernetes", "machine learning", "data analysis",
#         "project management", "agile", "scrum", "communication", "leadership",
#         "problem solving", "critical thinking", "teamwork"
#     ]
    
#     # Extract some skills from job description
#     job_skills = []
#     for skill in all_skills:
#         if skill.lower() in job_description.lower() or random.random() < 0.3:
#             job_skills.append(skill)
    
#     # Generate resume skills (some matching, some not)
#     resume_skills = []
#     for skill in all_skills:
#         if (skill in job_skills and random.random() < 0.7) or random.random() < 0.2:
#             resume_skills.append(skill)
    
#     # Calculate match score
#     match_score = (len(set(resume_skills).intersection(set(job_skills))) / len(job_skills)) * 100 if job_skills else 0
    
#     # Calculate ATS score (slightly higher than match score)
#     ats_score = min(100, match_score + random.uniform(5, 15))
    
#     # Generate missing skills
#     missing_skills = list(set(job_skills) - set(resume_skills))
    
#     # Generate improvement tips
#     improvement_tips = [
#         f"Add {skill} to your skills section" for skill in missing_skills[:3]
#     ]
    
#     improvement_tips.extend([
#         "Use more action verbs in your experience descriptions",
#         "Quantify your achievements with specific metrics",
#         "Tailor your resume summary to match the job description",
#         "Ensure your resume is ATS-friendly with standard section headings"
#     ])
    
#     # Generate interview questions
#     interview_questions = [
#         {
#             "question": f"Can you describe your experience with {random.choice(resume_skills)}?",
#             "sample_answer": f"I have used {random.choice(resume_skills)} in several projects, including developing a web application that improved efficiency by 30%."
#         },
#         {
#             "question": "Describe a challenging problem you solved in a previous role.",
#             "sample_answer": "In my previous role, I faced a database performance issue that was causing slow response times. I analyzed the queries, optimized indexes, and implemented caching, which reduced response time by 70%."
#         },
#         {
#             "question": f"How would you approach learning {random.choice(missing_skills) if missing_skills else 'a new technology'}?",
#             "sample_answer": "I would start by understanding the fundamentals through documentation and tutorials, then build a small project to apply what I've learned. I'd also join community forums to learn best practices."
#         }
#     ]
    
#     # Create result dictionary
#     result = {
#         "ats_score": ats_score,
#         "match_score": match_score,
#         "missing_skills": missing_skills,
#         "improvement_tips": improvement_tips,
#         "interview_questions": interview_questions,
#         "resume_skills": resume_skills,
#         "job_skills": job_skills
#     }
    
#     return result

# def main():
#     # Custom header with animation
#     col1, col2, col3 = st.columns([1, 2, 1])
#     with col2:
#         st.markdown("<h1 class='main-title'>AI-Powered Resume Analyzer</h1>", unsafe_allow_html=True)
#         st.markdown("<p class='subtitle'>Upload your resume and job description to get tailored insights and improvement tips.</p>", unsafe_allow_html=True)

#     # Create tabs for different sections
#     tab1, tab2, tab3 = st.tabs(["📄 Analyze Resume", "💬 Feedback", "ℹ️ About"])

#     with tab1:
#         col1, col2 = st.columns([1, 1])
        
#         with col1:
#             st.markdown("<div class='card animate-fade-in animate-delay-1'>", unsafe_allow_html=True)
#             st.markdown("<h3>Upload Your Resume</h3>", unsafe_allow_html=True)
#             st.markdown("<div class='upload-area'>", unsafe_allow_html=True)
#             resume_file = st.file_uploader("Choose a PDF or DOCX file", type=["pdf", "docx"], key="resume")
#             st.markdown("</div>", unsafe_allow_html=True)
#             st.markdown("</div>", unsafe_allow_html=True)

#         with col2:
#             st.markdown("<div class='card animate-fade-in animate-delay-2'>", unsafe_allow_html=True)
#             st.markdown("<h3>Job Description</h3>", unsafe_allow_html=True)
#             job_description = st.text_area("Paste job description here", height=250, key="job_desc")
#             st.markdown("</div>", unsafe_allow_html=True)

#         # Analyze button
#         col1, col2, col3 = st.columns([1, 2, 1])
#         with col2:
#             st.markdown("<div class='animate-fade-in animate-delay-3'>", unsafe_allow_html=True)
#             analyze_button = st.button("Analyze Resume", key="analyze")
#             st.markdown("</div>", unsafe_allow_html=True)

#         if analyze_button:
#             if job_description:
#                 with st.spinner("Analyzing your resume..."):
#                     if resume_file:
#                         # Use actual API if resume file is provided
#                         result = analyze_resume(resume_file, job_description)
#                     else:
#                         # Use simulation for demo purposes
#                         result = simulate_resume_analysis(job_description)
                    
#                     if result:
#                         st.session_state["analysis_result"] = result
#                         logging.info("Resume analysis completed successfully")
#             else:
#                 st.error("Please provide a job description.")
#                 logging.warning("Analysis attempted without job description")

#         # Display results if available
#         if "analysis_result" in st.session_state:
#             result = st.session_state["analysis_result"]
            
#             st.markdown("<h2 class='animate-fade-in'>Analysis Results</h2>", unsafe_allow_html=True)
            
#             # Score gauges
#             col1, col2 = st.columns(2)
#             with col1:
#                 st.markdown("<div class='card animate-fade-in'>", unsafe_allow_html=True)
#                 # FIXED: Properly passing both arguments to create_gauge_chart
#                 ats_fig = create_gauge_chart(result.get("ats_score", 0), "ATS Score")
#                 st.plotly_chart(ats_fig, use_container_width=True)
#                 st.markdown("</div>", unsafe_allow_html=True)
            
#             with col2:
#                 st.markdown("<div class='card animate-fade-in'>", unsafe_allow_html=True)
#                 match_fig = create_gauge_chart(result.get("match_score", 0), "Match Score")
#                 st.plotly_chart(match_fig, use_container_width=True)
#                 st.markdown("</div>", unsafe_allow_html=True)
            
#             # Skills visualization
#             st.markdown("<div class='card animate-fade-in'>", unsafe_allow_html=True)
#             st.markdown("<h3>Skills Analysis</h3>", unsafe_allow_html=True)
            
#             if "resume_skills" in result and "job_skills" in result:
#                 col1, col2 = st.columns([2, 1])
                
#                 with col1:
#                     radar_fig = create_skills_radar_chart(result.get("resume_skills", []), result.get("job_skills", []))
#                     st.plotly_chart(radar_fig, use_container_width=True)
                
#                 with col2:
#                     st.markdown("<h4>Skills Breakdown</h4>", unsafe_allow_html=True)
#                     skill_fig = create_skill_match_chart(result.get("resume_skills", []), result.get("job_skills", []))
#                     st.plotly_chart(skill_fig, use_container_width=True)
            
#             st.markdown("</div>", unsafe_allow_html=True)
            
#             # Missing Skills
#             st.markdown("<div class='card animate-fade-in'>", unsafe_allow_html=True)
#             with st.expander("Missing Skills", expanded=True):
#                 missing_skills = result.get("missing_skills", [])
#                 if missing_skills:
#                     st.markdown("<h4>Skills to consider adding to your resume:</h4>", unsafe_allow_html=True)
#                     st.markdown("<div class='skills-list'>", unsafe_allow_html=True)
#                     for skill in missing_skills:
#                         st.markdown(f"<span class='skill-tag'>{skill}</span>", unsafe_allow_html=True)
#                     st.markdown("</div>", unsafe_allow_html=True)
                    
#                     # Create a bar chart for missing skills
#                     missing_df = pd.DataFrame({
#                         'Skill': missing_skills,
#                         'Importance': np.random.uniform(0.5, 1.0, len(missing_skills))
#                     })
                    
#                     chart = alt.Chart(missing_df).mark_bar().encode(
#                         x=alt.X('Importance:Q', title='Relevance to Job'),
#                         y=alt.Y('Skill:N', sort='-x', title=None),
#                         color=alt.Color('Importance:Q', scale=alt.Scale(scheme='blues'), legend=None),
#                         tooltip=['Skill', 'Importance']
#                     ).properties(
#                         title='Missing Skills by Relevance',
#                         height=min(300, len(missing_skills) * 30)
#                     )
                    
#                     st.altair_chart(chart, use_container_width=True)
#                 else:
#                     st.success("No critical skills missing! Your resume matches the job requirements well.")
#             st.markdown("</div>", unsafe_allow_html=True)
            
#             # Improvement Tips
#             st.markdown("<div class='card animate-fade-in'>", unsafe_allow_html=True)
#             with st.expander("Improvement Tips", expanded=True):
#                 tips = result.get("improvement_tips", [])
#                 if tips:
#                     st.markdown("<h4>Actionable suggestions to enhance your resume:</h4>", unsafe_allow_html=True)
#                     st.markdown("<ul class='tips-list'>", unsafe_allow_html=True)
#                     for tip in tips:
#                         st.markdown(f"<li>{tip}</li>", unsafe_allow_html=True)
#                     st.markdown("</ul>", unsafe_allow_html=True)
#                 else:
#                     st.write("No specific improvement tips available.")
#             st.markdown("</div>", unsafe_allow_html=True)
            
#             # Interview Prep
#             st.markdown("<div class='card animate-fade-in'>", unsafe_allow_html=True)
#             with st.expander("Interview Preparation", expanded=True):
#                 questions = result.get("interview_questions", [])
#                 if questions:
#                     st.markdown("<h4>Mock interview questions and sample answers:</h4>", unsafe_allow_html=True)
#                     for i, q in enumerate(questions):
#                         with st.container():
#                             st.markdown(f"<div style='background-color: #f8fafc; padding: 15px; border-radius: 8px; margin-bottom: 15px;'>", unsafe_allow_html=True)
#                             st.markdown(f"<strong>Question {i+1}:</strong> {q['question']}", unsafe_allow_html=True)
#                             with st.expander("View Sample Answer"):
#                                 st.markdown(f"<div style='padding: 10px;'>{q['sample_answer']}</div>", unsafe_allow_html=True)
#                             st.markdown("</div>", unsafe_allow_html=True)
#                 else:
#                     st.write("No interview questions generated.")
#             st.markdown("</div>", unsafe_allow_html=True)

#     with tab2:
#         col1, col2 = st.columns([1, 2])
        
#         with col1:
#             st.image("https://img.icons8.com/color/96/000000/feedback.png", width=150)
        
#         with col2:
#             st.markdown("<h2>We Value Your Feedback</h2>", unsafe_allow_html=True)
#             st.markdown("<p>Help us improve the Resume Analyzer by sharing your thoughts and suggestions.</p>", unsafe_allow_html=True)
        
#         st.markdown("<div class='feedback-form'>", unsafe_allow_html=True)
#         with st.form(key="feedback_form"):
#             feedback = st.text_area("Your Feedback", height=100, placeholder="Share your thoughts or suggestions...")
            
#             # Custom rating UI
#             st.markdown("<p>Rate your experience:</p>", unsafe_allow_html=True)
#             rating = st.slider("Rate your experience", 1, 5, 3)
            
#             # Display stars based on rating
#             stars_html = ""
#             for i in range(1, 6):
#                 if i <= rating:
#                     stars_html += "★"
#                 else:
#                     stars_html += "☆"
            
#             st.markdown(f"<div style='font-size: 24px; color: #f59e0b;'>{stars_html}</div>", unsafe_allow_html=True)
            
#             submit_feedback = st.form_submit_button("Submit Feedback")
#             if submit_feedback:
#                 if feedback:
#                     success = save_feedback(feedback, rating)
#                     if success:
#                         st.success("Thank you for your feedback! We appreciate your input.")
                        
#                         # Show a celebratory animation
#                         st.balloons()
#                 else:
#                     st.error("Please provide feedback before submitting.")
#                     logging.warning("Feedback submission attempted without input")
#         st.markdown("</div>", unsafe_allow_html=True)
        
#         # Display feedback statistics
#         st.markdown("<div class='card' style='margin-top: 20px;'>", unsafe_allow_html=True)
#         st.markdown("<h3>Feedback Statistics</h3>", unsafe_allow_html=True)
        
#         # Simulate feedback data
#         feedback_data = {
#             "Ratings": [5, 4, 5, 3, 4, 5, 4, 3, 5, 4],
#             "Categories": ["UI/UX", "Accuracy", "Features", "Speed", "Usability"]
#         }
        
#         col1, col2 = st.columns(2)
        
#         with col1:
#             # Create a histogram of ratings
#             ratings_df = pd.DataFrame({"Rating": feedback_data["Ratings"]})
#             hist = alt.Chart(ratings_df).mark_bar().encode(
#                 x=alt.X("Rating:O", title="Rating"),
#                 y=alt.Y("count()", title="Count"),
#                 color=alt.Color("Rating:O", scale=alt.Scale(scheme="blues"))
#             ).properties(
#                 title="Rating Distribution"
#             )
#             st.altair_chart(hist, use_container_width=True)
        
#         with col2:
#             # Create a pie chart of feedback categories
#             categories_df = pd.DataFrame({
#                 "Category": feedback_data["Categories"],
#                 "Count": [3, 2, 2, 1, 2]
#             })
            
#             pie = alt.Chart(categories_df).mark_arc().encode(
#                 theta=alt.Theta("Count:Q"),
#                 color=alt.Color("Category:N", scale=alt.Scale(scheme="category10")),
#                 tooltip=["Category", "Count"]
#             ).properties(
#                 title="Feedback by Category"
#             )
#             st.altair_chart(pie, use_container_width=True)
        
#         st.markdown("</div>", unsafe_allow_html=True)

#     with tab3:
#         col1, col2 = st.columns([1, 2])
        
#         with col1:
#             st.image("https://img.icons8.com/color/96/000000/about.png", width=150)
        
#         with col2:
#             st.markdown("<h2>About the Resume Analyzer</h2>", unsafe_allow_html=True)
#             st.markdown("""
#             <p>The AI-Powered Resume Analyzer uses advanced artificial intelligence to analyze your resume against job descriptions, 
#             providing valuable insights to help you land your dream job.</p>
#             """, unsafe_allow_html=True)
        
#         st.markdown("<div class='about-section'>", unsafe_allow_html=True)
#         st.markdown("<h3>Key Features</h3>", unsafe_allow_html=True)
        
#         st.markdown("<div class='feature-grid'>", unsafe_allow_html=True)
        
#         features = [
#             {"icon": "📊", "title": "ATS Score", "description": "Evaluates resume compatibility with Applicant Tracking Systems."},
#             {"icon": "🎯", "title": "Match Score", "description": "Measures alignment with job requirements."},
#             {"icon": "💡", "title": "Improvement Tips", "description": "Provides actionable suggestions to enhance your resume."},
#             {"icon": "🗣️", "title": "Interview Prep", "description": "Generates tailored questions and sample answers."},
#             {"icon": "📈", "title": "Skills Analysis", "description": "Visualizes your skills compared to job requirements."},
#             {"icon": "🔍", "title": "Missing Skills", "description": "Identifies key skills to add to your resume."}
#         ]
        
#         for feature in features:
#             st.markdown(f"""
#             <div class='feature-card'>
#                 <div class='feature-icon'>{feature['icon']}</div>
#                 <div class='feature-title'>{feature['title']}</div>
#                 <p>{feature['description']}</p>
#             </div>
#             """, unsafe_allow_html=True)
        
#         st.markdown("</div>", unsafe_allow_html=True)
        
#         st.markdown("<h3 style='margin-top: 20px;'>Technology Stack</h3>", unsafe_allow_html=True)
        
#         col1, col2, col3 = st.columns(3)
        
#         with col1:
#             st.markdown("""
#             <div style='text-align: center;'>
#                 <h4>Frontend</h4>
#                 <ul style='list-style-type: none; padding: 0;'>
#                     <li>Streamlit</li>
#                     <li>Plotly</li>
#                     <li>Altair</li>
#                     <li>Custom CSS</li>
#                 </ul>
#             </div>
#             """, unsafe_allow_html=True)
        
#         with col2:
#             st.markdown("""
#             <div style='text-align: center;'>
#                 <h4>Backend</h4>
#                 <ul style='list-style-type: none; padding: 0;'>
#                     <li>FastAPI</li>
#                     <li>Python</li>
#                     <li>Sentence Transformers</li>
#                     <li>spaCy NLP</li>
#                 </ul>
#             </div>
#             """, unsafe_allow_html=True)
        
#         with col3:
#             st.markdown("""
#             <div style='text-align: center;'>
#                 <h4>AI Models</h4>
#                 <ul style='list-style-type: none; padding: 0;'>
#                     <li>DistilGPT2</li>
#                     <li>MiniLM-L6-v2</li>
#                     <li>Cosine Similarity</li>
#                     <li>Keyword Extraction</li>
#                 </ul>
#             </div>
#             """, unsafe_allow_html=True)
        
#         st.markdown("</div>", unsafe_allow_html=True)
        
#         # Usage statistics
#         st.markdown("<div class='card' style='margin-top: 20px;'>", unsafe_allow_html=True)
#         st.markdown("<h3>Usage Statistics</h3>", unsafe_allow_html=True)
        
#         # Create sample data
#         dates = pd.date_range(start='2023-01-01', periods=30, freq='D')
#         usage_data = pd.DataFrame({
#             'Date': dates,
#             'Resumes Analyzed': np.random.randint(10, 100, size=30),
#             'Unique Users': np.random.randint(5, 50, size=30)
#         })
        
#         # Create a line chart
#         line_chart = alt.Chart(usage_data).mark_line(point=True).encode(
#             x=alt.X('Date:T', title='Date'),
#             y=alt.Y('Resumes Analyzed:Q', title='Count'),
#             tooltip=['Date', 'Resumes Analyzed', 'Unique Users']
#         ).properties(
#             title='Resumes Analyzed Over Time'
#         )
        
#         st.altair_chart(line_chart, use_container_width=True)
        
#         # Display total statistics
#         col1, col2, col3 = st.columns(3)
        
#         with col1:
#             st.markdown(f"""
#             <div style='text-align: center; padding: 20px; background-color: #f8fafc; border-radius: 8px;'>
#                 <h4>Total Resumes</h4>
#                 <p style='font-size: 24px; font-weight: bold; color: #3b82f6;'>{usage_data['Resumes Analyzed'].sum()}</p>
#             </div>
#             """, unsafe_allow_html=True)
        
#         with col2:
#             st.markdown(f"""
#             <div style='text-align: center; padding: 20px; background-color: #f8fafc; border-radius: 8px;'>
#                 <h4>Unique Users</h4>
#                 <p style='font-size: 24px; font-weight: bold; color: #3b82f6;'>{usage_data['Unique Users'].sum() // 2}</p>
#             </div>
#             """, unsafe_allow_html=True)
        
#         with col3:
#             st.markdown(f"""
#             <div style='text-align: center; padding: 20px; background-color: #f8fafc; border-radius: 8px;'>
#                 <h4>Avg. Match Score</h4>
#                 <p style='font-size: 24px; font-weight: bold; color: #3b82f6;'>{67.8:.1f}%</p>
#             </div>
#             """, unsafe_allow_html=True)
        
#         st.markdown("</div>", unsafe_allow_html=True)

# if __name__ == "__main__":
#     main()

import streamlit as st
import requests
import os
import logging
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import time
from datetime import datetime
import random
import altair as alt

# Configure logging
logging.basicConfig(filename="streamlit.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Set page configuration
st.set_page_config(
    page_title="AI-Powered Resume Analyzer",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="📝"
)

# Load custom CSS
css_path = "static/styles.css"
if os.path.exists(css_path):
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    logging.info("Custom CSS loaded successfully")
else:
    logging.warning("Custom CSS file not found, using fallback CSS")
    st.warning("Custom CSS file not found. Please create the file at 'static/styles.css' for the best experience.")

# Cache function for resume analysis
@st.cache_data
def analyze_resume(file, job_description):
    try:
        files = {"file": file}
        data = {"text": job_description}
        response = requests.post("http://localhost:8000/analyze", files=files, data=data)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        logging.error(f"Error analyzing resume: {str(e)}")
        st.error(f"Error analyzing resume: {str(e)}")
        return None

# Function to save feedback
def save_feedback(feedback, rating):
    try:
        with open("feedback.txt", "a") as f:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"[{timestamp}] Rating: {rating}/5\nFeedback: {feedback}\n\n")
        logging.info("Feedback saved successfully")
        return True
    except Exception as e:
        logging.error(f"Error saving feedback: {str(e)}")
        st.error(f"Error saving feedback: {str(e)}")
        return False

# Function to create a radar chart for skills
def create_skills_radar_chart(resume_skills, job_skills):
    # Create a set of all skills
    all_skills = set(resume_skills + job_skills)
    
    # Create data for the radar chart
    categories = list(all_skills)
    resume_values = [1 if skill in resume_skills else 0 for skill in categories]
    job_values = [1 if skill in job_skills else 0 for skill in categories]
    
    # Create the radar chart
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=resume_values,
        theta=categories,
        fill='toself',
        name='Your Resume',
        line_color='#3b82f6',
        fillcolor='rgba(59, 130, 246, 0.2)'
    ))
    
    fig.add_trace(go.Scatterpolar(
        r=job_values,
        theta=categories,
        fill='toself',
        name='Job Requirements',
        line_color='#1e3a8a',
        fillcolor='rgba(30, 58, 138, 0.2)'
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 1]
            )
        ),
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.1,
            xanchor="center",
            x=0.5
        ),
        height=500,
        margin=dict(l=80, r=80, t=20, b=20),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    
    return fig

# Function to create a score gauge chart
def create_gauge_chart(score, title):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': title, 'font': {'size': 24, 'color': '#1e3a8a', 'family': 'Montserrat'}},
        gauge={
            'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "#1e3a8a"},
            'bar': {'color': "#3b82f6"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "#1e3a8a",
            'steps': [
                {'range': [0, 30], 'color': 'rgba(255, 99, 132, 0.3)'},
                {'range': [30, 70], 'color': 'rgba(255, 205, 86, 0.3)'},
                {'range': [70, 100], 'color': 'rgba(75, 192, 192, 0.3)'}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 90
            }
        }
    ))
    
    fig.update_layout(
        height=300,
        margin=dict(l=20, r=20, t=50, b=20),
        paper_bgcolor='rgba(0,0,0,0)',
        font={'color': "#1e3a8a", 'family': "Montserrat"}
    )
    
    return fig

# Function to create a bar chart for skill match
def create_skill_match_chart(resume_skills, job_skills):
    # Count the number of skills in each category
    resume_count = len(resume_skills)
    job_count = len(job_skills)
    matched_count = len(set(resume_skills).intersection(set(job_skills)))
    missing_count = job_count - matched_count
    
    # Create data for the bar chart
    categories = ['Resume Skills', 'Job Skills', 'Matched Skills', 'Missing Skills']
    values = [resume_count, job_count, matched_count, missing_count]
    colors = ['#3b82f6', '#1e3a8a', '#10b981', '#ef4444']
    
    # Create the bar chart
    fig = go.Figure(go.Bar(
        x=categories,
        y=values,
        marker_color=colors,
        text=values,
        textposition='auto'
    ))
    
    fig.update_layout(
        title={
            'text': 'Skills Analysis',
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {'size': 20, 'color': '#1e3a8a', 'family': 'Montserrat'}
        },
        xaxis_title="Categories",
        yaxis_title="Count",
        height=400,
        margin=dict(l=20, r=20, t=80, b=20),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font={'color': "#1e3a8a", 'family': "Montserrat"}
    )
    
    return fig

# Function to simulate resume analysis for demo purposes
def simulate_resume_analysis(job_description):
    # Simulate processing time
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    for i in range(101):
        # Update progress bar
        progress_bar.progress(i)
        
        # Update status text based on progress
        if i < 20:
            status_text.text("Extracting text from resume...")
        elif i < 40:
            status_text.text("Analyzing resume structure...")
        elif i < 60:
            status_text.text("Identifying skills and experience...")
        elif i < 80:
            status_text.text("Comparing with job description...")
        else:
            status_text.text("Finalizing analysis...")
        
        time.sleep(0.05)
    
    # Clear progress indicators
    progress_bar.empty()
    status_text.empty()
    
    # Generate sample skills
    all_skills = [
        "python", "java", "javascript", "react", "node.js", "mongodb",
        "sql", "aws", "docker", "kubernetes", "machine learning", "data analysis",
        "project management", "agile", "scrum", "communication", "leadership",
        "problem solving", "critical thinking", "teamwork"
    ]
    
    # Extract some skills from job description
    job_skills = []
    for skill in all_skills:
        if skill.lower() in job_description.lower() or random.random() < 0.3:
            job_skills.append(skill)
    
    # Generate resume skills (some matching, some not)
    resume_skills = []
    for skill in all_skills:
        if (skill in job_skills and random.random() < 0.7) or random.random() < 0.2:
            resume_skills.append(skill)
    
    # Calculate match score
    match_score = (len(set(resume_skills).intersection(set(job_skills))) / len(job_skills)) * 100 if job_skills else 0
    
    # Calculate ATS score (slightly higher than match score)
    ats_score = min(100, match_score + random.uniform(5, 15))
    
    # Generate missing skills
    missing_skills = list(set(job_skills) - set(resume_skills))
    
    # Generate improvement tips
    improvement_tips = [
        f"Add {skill} to your skills section" for skill in missing_skills[:3]
    ]
    
    improvement_tips.extend([
        "Use more action verbs in your experience descriptions",
        "Quantify your achievements with specific metrics",
        "Tailor your resume summary to match the job description",
        "Ensure your resume is ATS-friendly with standard section headings"
    ])
    
    # Generate interview questions
    interview_questions = [
        {
            "question": f"Can you describe your experience with {random.choice(resume_skills)}?",
            "sample_answer": f"I have used {random.choice(resume_skills)} in several projects, including developing a web application that improved efficiency by 30%."
        },
        {
            "question": "Describe a challenging problem you solved in a previous role.",
            "sample_answer": "In my previous role, I faced a database performance issue that was causing slow response times. I analyzed the queries, optimized indexes, and implemented caching, which reduced response time by 70%."
        },
        {
            "question": f"How would you approach learning {random.choice(missing_skills) if missing_skills else 'a new technology'}?",
            "sample_answer": "I would start by understanding the fundamentals through documentation and tutorials, then build a small project to apply what I've learned. I'd also join community forums to learn best practices."
        }
    ]
    
    # Create result dictionary
    result = {
        "ats_score": ats_score,
        "match_score": match_score,
        "missing_skills": missing_skills,
        "improvement_tips": improvement_tips,
        "interview_questions": interview_questions,
        "resume_skills": resume_skills,
        "job_skills": job_skills
    }
    
    return result

def main():
    # Custom header with animation
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<h1 class='main-title'>AI-Powered Resume Analyzer</h1>", unsafe_allow_html=True)
        st.markdown("<p class='subtitle'>Upload your resume and job description to get tailored insights and improvement tips.</p>", unsafe_allow_html=True)

    # Create tabs for different sections
    tab1, tab2, tab3 = st.tabs(["📄 Analyze Resume", "💬 Feedback", "ℹ️ About"])

    with tab1:
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("<div class='card animate-fade-in animate-delay-1'>", unsafe_allow_html=True)
            st.markdown("<h3>Upload Your Resume</h3>", unsafe_allow_html=True)
            st.markdown("<div class='upload-area'>", unsafe_allow_html=True)
            resume_file = st.file_uploader("Choose a PDF or DOCX file", type=["pdf", "docx"], key="resume")
            st.markdown("</div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

        with col2:
            st.markdown("<div class='card animate-fade-in animate-delay-2'>", unsafe_allow_html=True)
            st.markdown("<h3>Job Description</h3>", unsafe_allow_html=True)
            job_description = st.text_area("Paste job description here", height=250, key="job_desc")
            st.markdown("</div>", unsafe_allow_html=True)

        # Analyze button
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown("<div class='animate-fade-in animate-delay-3'>", unsafe_allow_html=True)
            analyze_button = st.button("Analyze Resume", key="analyze")
            st.markdown("</div>", unsafe_allow_html=True)

        if analyze_button:
            if job_description:
                with st.spinner("Analyzing your resume..."):
                    if resume_file:
                        # Use actual API if resume file is provided
                        result = analyze_resume(resume_file, job_description)
                    else:
                        # Use simulation for demo purposes
                        result = simulate_resume_analysis(job_description)
                    
                    if result:
                        st.session_state["analysis_result"] = result
                        logging.info("Resume analysis completed successfully")
            else:
                st.error("Please provide a job description.")
                logging.warning("Analysis attempted without job description")

        # Display results if available
        if "analysis_result" in st.session_state:
            result = st.session_state["analysis_result"]
            
            st.markdown("<h2 class='animate-fade-in'>Analysis Results</h2>", unsafe_allow_html=True)
            
            # Score gauges
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("<div class='card animate-fade-in'>", unsafe_allow_html=True)
                # FIXED: Properly passing both arguments to create_gauge_chart
                ats_fig = create_gauge_chart(result.get("ats_score", 0), "ATS Score")
                st.plotly_chart(ats_fig, use_container_width=True)
                st.markdown("</div>", unsafe_allow_html=True)
            
            with col2:
                st.markdown("<div class='card animate-fade-in'>", unsafe_allow_html=True)
                match_fig = create_gauge_chart(result.get("match_score", 0), "Match Score")
                st.plotly_chart(match_fig, use_container_width=True)
                st.markdown("</div>", unsafe_allow_html=True)
            
            # Skills visualization
            st.markdown("<div class='card animate-fade-in'>", unsafe_allow_html=True)
            st.markdown("<h3>Skills Analysis</h3>", unsafe_allow_html=True)
            
            if "resume_skills" in result and "job_skills" in result:
                col1, col2 = st.columns([2, 1])
                
                with col1:
                    radar_fig = create_skills_radar_chart(result.get("resume_skills", []), result.get("job_skills", []))
                    st.plotly_chart(radar_fig, use_container_width=True)
                
                with col2:
                    st.markdown("<h4>Skills Breakdown</h4>", unsafe_allow_html=True)
                    skill_fig = create_skill_match_chart(result.get("resume_skills", []), result.get("job_skills", []))
                    st.plotly_chart(skill_fig, use_container_width=True)
            
            st.markdown("</div>", unsafe_allow_html=True)
            
            # Missing Skills
            st.markdown("<div class='card animate-fade-in'>", unsafe_allow_html=True)
            with st.expander("Missing Skills", expanded=True):
                missing_skills = result.get("missing_skills", [])
                if missing_skills:
                    st.markdown("<h4>Skills to consider adding to your resume:</h4>", unsafe_allow_html=True)
                    st.markdown("<div class='skills-list'>", unsafe_allow_html=True)
                    for skill in missing_skills:
                        st.markdown(f"<span class='skill-tag'>{skill}</span>", unsafe_allow_html=True)
                    st.markdown("</div>", unsafe_allow_html=True)
                    
                    # Create a bar chart for missing skills
                    missing_df = pd.DataFrame({
                        'Skill': missing_skills,
                        'Importance': np.random.uniform(0.5, 1.0, len(missing_skills))
                    })
                    
                    chart = alt.Chart(missing_df).mark_bar().encode(
                        x=alt.X('Importance:Q', title='Relevance to Job'),
                        y=alt.Y('Skill:N', sort='-x', title=None),
                        color=alt.Color('Importance:Q', scale=alt.Scale(scheme='blues'), legend=None),
                        tooltip=['Skill', 'Importance']
                    ).properties(
                        title='Missing Skills by Relevance',
                        height=min(300, len(missing_skills) * 30)
                    )
                    
                    st.altair_chart(chart, use_container_width=True)
                else:
                    st.success("No critical skills missing! Your resume matches the job requirements well.")
            st.markdown("</div>", unsafe_allow_html=True)
            
            # Improvement Tips
            st.markdown("<div class='card animate-fade-in'>", unsafe_allow_html=True)
            with st.expander("Improvement Tips", expanded=True):
                tips = result.get("improvement_tips", [])
                if tips:
                    st.markdown("<h4>Actionable suggestions to enhance your resume:</h4>", unsafe_allow_html=True)
                    st.markdown("<ul class='tips-list'>", unsafe_allow_html=True)
                    for tip in tips:
                        st.markdown(f"<li>{tip}</li>", unsafe_allow_html=True)
                    st.markdown("</ul>", unsafe_allow_html=True)
                else:
                    st.write("No specific improvement tips available.")
            st.markdown("</div>", unsafe_allow_html=True)
            
            # Interview Prep
            st.markdown("<div class='card animate-fade-in'>", unsafe_allow_html=True)
            st.markdown("<h4>Interview Preparation</h4>", unsafe_allow_html=True)
            questions = result.get("interview_questions", [])
            if questions:
                st.markdown("<h5>Mock interview questions and sample answers:</h5>", unsafe_allow_html=True)
                for i, q in enumerate(questions):
                    with st.container():
                        st.markdown(f"<div class='question-card'>", unsafe_allow_html=True)
                        st.markdown(f"<strong>Question {i+1}:</strong> {q['question']}", unsafe_allow_html=True)
                        # Instead of using a nested expander, use a collapsible div with JavaScript
                        st.markdown(f"""
                        <details class="sample-answer">
                            <summary>View Sample Answer</summary>
                            <div class="answer-content">{q['sample_answer']}</div>
                        </details>
                        """, unsafe_allow_html=True)
                        st.markdown("</div>", unsafe_allow_html=True)
            else:
                st.write("No interview questions generated.")
            st.markdown("</div>", unsafe_allow_html=True)

    with tab2:
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.image("https://img.icons8.com/color/96/000000/feedback.png", width=150)
        
        with col2:
            st.markdown("<h2>We Value Your Feedback</h2>", unsafe_allow_html=True)
            st.markdown("<p>Help us improve the Resume Analyzer by sharing your thoughts and suggestions.</p>", unsafe_allow_html=True)
        
        st.markdown("<div class='feedback-form'>", unsafe_allow_html=True)
        with st.form(key="feedback_form"):
            feedback = st.text_area("Your Feedback", height=100, placeholder="Share your thoughts or suggestions...")
            
            # Custom rating UI
            st.markdown("<p>Rate your experience:</p>", unsafe_allow_html=True)
            rating = st.slider("Rate your experience", 1, 5, 3)
            
            # Display stars based on rating
            stars_html = ""
            for i in range(1, 6):
                if i <= rating:
                    stars_html += "★"
                else:
                    stars_html += "☆"
            
            st.markdown(f"<div style='font-size: 24px; color: #f59e0b;'>{stars_html}</div>", unsafe_allow_html=True)
            
            submit_feedback = st.form_submit_button("Submit Feedback")
            if submit_feedback:
                if feedback:
                    success = save_feedback(feedback, rating)
                    if success:
                        st.success("Thank you for your feedback! We appreciate your input.")
                        
                        # Show a celebratory animation
                        st.balloons()
                else:
                    st.error("Please provide feedback before submitting.")
                    logging.warning("Feedback submission attempted without input")
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Display feedback statistics
        st.markdown("<div class='card' style='margin-top: 20px;'>", unsafe_allow_html=True)
        st.markdown("<h3>Feedback Statistics</h3>", unsafe_allow_html=True)
        
        # Simulate feedback data
        feedback_data = {
            "Ratings": [5, 4, 5, 3, 4, 5, 4, 3, 5, 4],
            "Categories": ["UI/UX", "Accuracy", "Features", "Speed", "Usability"]
        }
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Create a histogram of ratings
            ratings_df = pd.DataFrame({"Rating": feedback_data["Ratings"]})
            hist = alt.Chart(ratings_df).mark_bar().encode(
                x=alt.X("Rating:O", title="Rating"),
                y=alt.Y("count()", title="Count"),
                color=alt.Color("Rating:O", scale=alt.Scale(scheme="blues"))
            ).properties(
                title="Rating Distribution"
            )
            st.altair_chart(hist, use_container_width=True)
        
        with col2:
            # Create a pie chart of feedback categories
            categories_df = pd.DataFrame({
                "Category": feedback_data["Categories"],
                "Count": [3, 2, 2, 1, 2]
            })
            
            pie = alt.Chart(categories_df).mark_arc().encode(
                theta=alt.Theta("Count:Q"),
                color=alt.Color("Category:N", scale=alt.Scale(scheme="category10")),
                tooltip=["Category", "Count"]
            ).properties(
                title="Feedback by Category"
            )
            st.altair_chart(pie, use_container_width=True)
        
        st.markdown("</div>", unsafe_allow_html=True)

    with tab3:
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.image("https://img.icons8.com/color/96/000000/about.png", width=150)
        
        with col2:
            st.markdown("<h2>About the Resume Analyzer</h2>", unsafe_allow_html=True)
            st.markdown("""
            <p>The AI-Powered Resume Analyzer uses advanced artificial intelligence to analyze your resume against job descriptions, 
            providing valuable insights to help you land your dream job.</p>
            """, unsafe_allow_html=True)
        
        st.markdown("<div class='about-section'>", unsafe_allow_html=True)
        st.markdown("<h3>Key Features</h3>", unsafe_allow_html=True)
        
        st.markdown("<div class='feature-grid'>", unsafe_allow_html=True)
        
        features = [
            {"icon": "📊", "title": "ATS Score", "description": "Evaluates resume compatibility with Applicant Tracking Systems."},
            {"icon": "🎯", "title": "Match Score", "description": "Measures alignment with job requirements."},
            {"icon": "💡", "title": "Improvement Tips", "description": "Provides actionable suggestions to enhance your resume."},
            {"icon": "🗣️", "title": "Interview Prep", "description": "Generates tailored questions and sample answers."},
            {"icon": "📈", "title": "Skills Analysis", "description": "Visualizes your skills compared to job requirements."},
            {"icon": "🔍", "title": "Missing Skills", "description": "Identifies key skills to add to your resume."}
        ]
        
        for feature in features:
            st.markdown(f"""
            <div class='feature-card'>
                <div class='feature-icon'>{feature['icon']}</div>
                <div class='feature-title'>{feature['title']}</div>
                <p>{feature['description']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("<h3 style='margin-top: 20px;'>Technology Stack</h3>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div style='text-align: center;'>
                <h4>Frontend</h4>
                <ul style='list-style-type: none; padding: 0;'>
                    <li>Streamlit</li>
                    <li>Plotly</li>
                    <li>Altair</li>
                    <li>Custom CSS</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div style='text-align: center;'>
                <h4>Backend</h4>
                <ul style='list-style-type: none; padding: 0;'>
                    <li>FastAPI</li>
                    <li>Python</li>
                    <li>Sentence Transformers</li>
                    <li>spaCy NLP</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div style='text-align: center;'>
                <h4>AI Models</h4>
                <ul style='list-style-type: none; padding: 0;'>
                    <li>DistilGPT2</li>
                    <li>MiniLM-L6-v2</li>
                    <li>Cosine Similarity</li>
                    <li>Keyword Extraction</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Usage statistics
        st.markdown("<div class='card' style='margin-top: 20px;'>", unsafe_allow_html=True)
        st.markdown("<h3>Usage Statistics</h3>", unsafe_allow_html=True)
        
        # Create sample data
        dates = pd.date_range(start='2023-01-01', periods=30, freq='D')
        usage_data = pd.DataFrame({
            'Date': dates,
            'Resumes Analyzed': np.random.randint(10, 100, size=30),
            'Unique Users': np.random.randint(5, 50, size=30)
        })
        
        # Create a line chart
        line_chart = alt.Chart(usage_data).mark_line(point=True).encode(
            x=alt.X('Date:T', title='Date'),
            y=alt.Y('Resumes Analyzed:Q', title='Count'),
            tooltip=['Date', 'Resumes Analyzed', 'Unique Users']
        ).properties(
            title='Resumes Analyzed Over Time'
        )
        
        st.altair_chart(line_chart, use_container_width=True)
        
        # Display total statistics
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown(f"""
            <div style='text-align: center; padding: 20px; background-color: #f8fafc; border-radius: 8px;'>
                <h4>Total Resumes</h4>
                <p style='font-size: 24px; font-weight: bold; color: #3b82f6;'>{usage_data['Resumes Analyzed'].sum()}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div style='text-align: center; padding: 20px; background-color: #f8fafc; border-radius: 8px;'>
                <h4>Unique Users</h4>
                <p style='font-size: 24px; font-weight: bold; color: #3b82f6;'>{usage_data['Unique Users'].sum() // 2}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown(f"""
            <div style='text-align: center; padding: 20px; background-color: #f8fafc; border-radius: 8px;'>
                <h4>Avg. Match Score</h4>
                <p style='font-size: 24px; font-weight: bold; color: #3b82f6;'>{67.8:.1f}%</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()