import re

def extract_salary_range(description):
    pattern = r"\$?\d{2,3}[,]?\d{0,3}\s?(?:to|-)?\s?\$?\d{2,3}[,]?\d{0,3}"
    matches = re.findall(pattern, description.lower())
    return matches[0] if matches else "Not mentioned"
