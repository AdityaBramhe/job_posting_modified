from scraper import scrape_page
from pymongo import MongoClient
import argparse


def save_to_mongo(jobs, db_url, db_name="job_posting_modified", collection_name="ScrapedJobs"):
    client = MongoClient(db_url)
    db = client[db_name]
    collection = db[collection_name]

    # clear old data for clean simulation runs
    collection.delete_many({})

    if jobs:
        collection.insert_many(jobs)
        print(f"✅ Inserted {len(jobs)} jobs into MongoDB.")
    else:
        print("⚠️ No jobs to insert.")


def run_agent1():
    """
    Agent 1: Synthetic Data Generator
    Replaces scraping with simulated job postings
    """

    all_jobs = []

    # dummy URLs (not used, but keeps structure same)
    urls = ["synthetic_page_1", "synthetic_page_2"]

    for url in urls:
        jobs = scrape_page(url)  # now returns structured synthetic jobs
        all_jobs.extend(jobs)

    return all_jobs


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--runs", type=int, default=1, help="Number of simulation runs")
    args = parser.parse_args()

    mongo_url = "REMOVEDadityabramhe7:Adi031204@cluster0.is9smo4.mongodb.net/job_posting_modified"

    all_jobs = []

    for i in range(args.runs):
        print(f"\n🚀 Simulation Run {i+1}")
        jobs = run_agent1()
        all_jobs.extend(jobs)

    print(f"\n📊 Total synthetic jobs generated: {len(all_jobs)}")

    save_to_mongo(all_jobs, mongo_url)