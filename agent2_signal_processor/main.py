from pymongo import MongoClient
from signal_extraction import extract_tech_stack, classify_department
from urgency_detector import detect_urgency
from salary_parser import extract_salary_range
from datetime import datetime

def process_jobs(mongo_url, limit=16):
    client = MongoClient(mongo_url)
    db = client["JobPosting"]
    source_collection = db["ScrapedJobs"]
    signal_collection = db["ProcessedSignals"]

    # ✅ Only load last `limit` inserted jobs
    jobs_cursor = source_collection.find().sort([("_id", -1)]).limit(limit)
    jobs = list(jobs_cursor)

    processed = []

    for job in jobs:
        description = job.get("description", "")
        tech_stack = extract_tech_stack(description)
        is_urgent = detect_urgency(description)
        department = classify_department(job.get("title", ""))
        salary = extract_salary_range(description)

        processed_job = {
            "company": job.get("company"),
            "title": job.get("title"),
            "location": job.get("location"),
            "tech_stack": tech_stack,
            "is_urgent": is_urgent,
            "department": department,
            "salary_estimate": salary,
            "scraped_date": job.get("scraped_date", datetime.now().strftime("%Y-%m-%d"))
        }
        processed.append(processed_job)

    if processed:
        signal_collection.insert_many(processed)
        print(f"✅ Inserted {len(processed)} processed signals.")
    else:
        print("⚠️ No signals to process.")

if __name__ == "__main__":
    mongo_url = "REMOVEDadityabramhe7:C3kg0TDi21QaKOAM@jobposting.tgcylyz.mongodb.net/"
    process_jobs(mongo_url, limit=16)
