# scraper.py

import random
from datetime import datetime, timedelta


# --- synthetic pools ---
job_titles = [
    "Backend Engineer", "Frontend Developer", "Data Scientist",
    "ML Engineer", "DevOps Engineer", "Product Manager"
]

companies = ["Google", "Amazon", "Microsoft", "Flipkart", "Swiggy", "Zomato"]

locations = ["Bangalore", "Hyderabad", "Remote", "Pune", "Chennai"]

skills_pool = [
    "Python", "Java", "C++", "AWS", "Docker",
    "Kubernetes", "React", "Node.js", "SQL", "TensorFlow"
]


def generate_fake_job():
    import random
    from datetime import datetime, timedelta

    title = random.choice([
        "Backend Engineer", "ML Engineer", "Data Scientist",
        "Frontend Developer", "DevOps Engineer"
    ])

    skills_pool = [
        "Python", "AWS", "Docker", "TensorFlow",
        "React", "SQL", "Kubernetes"
    ]

    skills = random.sample(skills_pool, k=3)

    # 🔥 ADD URGENCY SIGNAL
    urgency_phrases = [
        "Immediate hiring",
        "Looking for candidates ASAP",
        "Urgent requirement",
        ""
    ]

    urgency_text = random.choice(urgency_phrases)

    return {
        "title": title,
        "company": random.choice(["Amazon", "Google", "Microsoft", "Flipkart", "Swiggy"]),
        "location": random.choice(["Bangalore", "Remote", "Chennai"]),
        "skills": skills,
        "salary": "10-25 LPA",
        "experience": f"{random.randint(1, 6)}+ years",
        "posted_date": datetime.now().strftime("%Y-%m-%d"),
        "description": f"{urgency_text}. Hiring {title} with {', '.join(skills)}."
    }


def scrape_page(url: str):
    jobs = []

    for i in range(20):
        job = generate_fake_job()

        # simulate Amazon aggressive hiring
        if i < 10:
            job["company"] = "Amazon"

        jobs.append(job)

    return jobs

    # simulate multiple jobs per "page"
    jobs = [generate_fake_job() for _ in range(random.randint(5, 10))]

    return jobs