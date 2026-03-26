# process_jobs.py

import os
from pymongo import MongoClient
from datetime import datetime
from signal_extractor import (
    extract_skills,
    extract_seniority,
    extract_department,
    extract_salary
)
from urgency_detector import detect_urgency
from dotenv import load_dotenv

# ✅ Load env first
load_dotenv()

# ✅ Use consistent variable name
MONGO_URI = os.getenv("MONGO_URI")

def process_jobs(limit=50):
    client = MongoClient(MONGO_URI)   # ✅ FIXED

    db = client["job_posting_modified"]

    # ✅ Correct collections
    source_collection = db["ScrapedJobs"]
    signal_collection = db["job_signals"]

    # ✅ Fetch jobs
    jobs = list(source_collection.find().limit(limit))

    print(f"🔍 Jobs fetched from DB: {len(jobs)}")

    # ✅ Debug sample
    if jobs:
        print("🧪 Sample job:", jobs[0])
    else:
        print("❌ No jobs found in ScrapedJobs collection")

    processed = []

    for job in jobs:
        description = job.get("description", "")
        title = job.get("title", "")

        signals = {
            "job_id": str(job.get("_id")),
            "title": title,
            "company": job.get("company", "Unknown"),
            "department": extract_department(title),
            "skills": extract_skills(description),
            "salary": extract_salary(description),
            "seniority": extract_seniority(description),
            "location": job.get("location", "Unknown"),
            "urgency": "Immediate" if detect_urgency(description) else "Not urgent",
            "num_roles": 1,
            "processed_at": datetime.now().strftime("%Y-%m-%d")
        }

        processed.append(signals)

    # ✅ Clear old signals
    signal_collection.delete_many({})

    if processed:
        signal_collection.insert_many(processed)
        print(f"✅ Processed {len(processed)} jobs into signals.")
    else:
        print("⚠️ No jobs processed.")