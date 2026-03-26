import json
import os
from dotenv import load_dotenv
from pymongo import MongoClient

# Load environment variables
load_dotenv()

# =========================
# MongoDB Configuration
# =========================
MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME", "job_posting_modified")
RAW_JOBS_COLLECTION = "raw_jobs"

# Safety check (important)
if not MONGO_URI:
    raise ValueError("MONGO_URI not set in environment variables")

# Initialize MongoDB client
client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[RAW_JOBS_COLLECTION]

# =========================
# Source Registry Loader
# =========================
def load_sources():
    """
    Loads job sources from config/sources.json
    Returns a list of source dictionaries
    """
    config_path = os.path.join("config", "sources.json")

    if not os.path.exists(config_path):
        raise FileNotFoundError(
            "sources.json not found. Please create config/sources.json"
        )

    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)

# =========================
# Example Processing Function
# =========================
def fetch_all_jobs():
    """
    Fetch all jobs from MongoDB raw_jobs collection
    """
    try:
        jobs = list(collection.find({}))
        print(f"[INFO] Fetched {len(jobs)} jobs from DB")
        return jobs
    except Exception as e:
        print(f"[ERROR] Failed to fetch jobs: {e}")
        return []

# =========================
# Main Runner (for testing)
# =========================
if __name__ == "__main__":
    sources = load_sources()
    print(f"[INFO] Loaded {len(sources)} sources")

    jobs = fetch_all_jobs()