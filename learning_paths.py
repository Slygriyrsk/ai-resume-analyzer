def get_learning_paths(missing_skills):
    # Static resource list (replace with SerpAPI in production)
    resources = {
        "Python": ["Coursera: Python for Everybody", "YouTube: Python Crash Course"],
        "AWS": ["AWS Skill Builder: AWS Fundamentals", "Coursera: AWS Cloud Practitioner"],
        "Docker": ["Docker Official Tutorials", "Udemy: Docker Mastery"],
        "SQL": ["Khan Academy: SQL Basics", "Mode Analytics: SQL Tutorial"],
        "Kubernetes": ["KodeKloud: Kubernetes for Beginners", "Coursera: Kubernetes Essentials"],
        "JavaScript": ["freeCodeCamp: JavaScript Course", "YouTube: JavaScript Tutorial"],
        "React": ["React Official Tutorial", "Scrimba: Learn React"],
        "Java": ["Oracle: Java Tutorials", "Udemy: Java Programming Masterclass"]
    }
    
    learning_paths = {}
    for skill in missing_skills[:2]:
        learning_paths[skill] = resources.get(skill, ["Search for free tutorials online"])
    return learning_paths