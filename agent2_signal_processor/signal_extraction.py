TECH_KEYWORDS = ["python", "pytorch", "tensorflow", "aws", "react", "node", "docker", "gcp"]

def extract_tech_stack(description):
    description = description.lower()
    return [tech for tech in TECH_KEYWORDS if tech in description]

def classify_department(title):
    title = title.lower()
    if "engineer" in title or "developer" in title or "data" in title:
        return "Tech"
    elif "marketing" in title:
        return "Marketing"
    elif "sales" in title:
        return "Sales"
    else:
        return "Other"
