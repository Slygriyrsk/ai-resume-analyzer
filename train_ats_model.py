import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import TfidfVectorizer
from xgboost import XGBClassifier
import pickle
import warnings
import numpy as np

# Suppress xgboost warnings
warnings.filterwarnings("ignore", category=FutureWarning)

# Load synthetic dataset
try:
    data = pd.read_csv("data/synthetic_ats_data.csv")
except FileNotFoundError:
    print("Error: synthetic_ats_data.csv not found. Run generate_synthetic_data.py first.")
    exit(1)

# Validate dataset
if data.empty or not all(col in data for col in ["keyword_score", "length", "has_skills_section", "action_verbs", "label"]):
    print("Error: Invalid dataset. Ensure synthetic_ats_data.csv contains required columns.")
    exit(1)

# Check for NaN or infinite values
if data[["keyword_score", "length", "has_skills_section", "action_verbs"]].isna().any().any():
    print("Warning: NaN values detected in features. Filling with zeros.")
    data.fillna(0, inplace=True)
if not np.isfinite(data[["keyword_score", "length", "has_skills_section", "action_verbs"]]).all().all():
    print("Warning: Infinite values detected in features. Replacing with zeros.")
    data.replace([np.inf, -np.inf], 0, inplace=True)

# Features and labels
X = data[["keyword_score", "length", "has_skills_section", "action_verbs"]]
y = data["label"]

# Split and train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = XGBClassifier(n_estimators=100, random_state=42, base_score=0.5)
try:
    model.fit(X_train, y_train)
except Exception as e:
    print(f"Error during model training: {str(e)}")
    exit(1)

# Evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# Save model and vectorizer
with open("models/ats_model.pkl", "wb") as f:
    pickle.dump(model, f)
with open("models/tfidf_vectorizer.pkl", "wb") as f:
    vectorizer = TfidfVectorizer(stop_words="english")
    vectorizer.fit(data["resume_text"] + " " + data["job_description"])
    pickle.dump(vectorizer, f)

print("Model and vectorizer saved to models/")