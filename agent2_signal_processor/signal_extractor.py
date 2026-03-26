# signal_extractor.py

import re

SKILLS_DB = [
    'python', 'sql', 'machine learning', 'deep learning', 'tensorflow',
    'pytorch', 'aws', 'docker', 'kubernetes', 'react', 'node.js'
]

def extract_skills(text):
    text = text.lower()
    return [skill for skill in SKILLS_DB if skill in text]


def extract_seniority(text):
    text = text.lower()
    if "senior" in text:
        return "Senior"
    elif "junior" in text:
        return "Junior"
    elif "intern" in text:
        return "Intern"
    elif "lead" in text:
        return "Lead"
    else:
        return "Mid"


def extract_department(title):
    title = title.lower()
    if "data" in title or "ml" in title:
        return "Data"
    elif "engineer" in title or "developer" in title:
        return "Engineering"
    elif "manager" in title:
        return "Management"
    else:
        return "General"


def extract_salary(text):
    match = re.search(r'(\d{1,2})-(\d{1,2})\s*lpa', text.lower())
    if match:
        return f"{match.group(1)}-{match.group(2)} LPA"
    return "Unknown"