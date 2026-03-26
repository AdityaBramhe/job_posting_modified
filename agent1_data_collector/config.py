import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# =========================
# MongoDB Configuration
# =========================
MONGO_URI = os.getenv("MONGO_URI", "REMOVEDadityabramhe7:Adi031204@cluster0.is9smo4.mongodb.net/job_posting_modified")
DB_NAME = os.getenv("DB_NAME", "job_posting_modified")
RAW_JOBS_COLLECTION = "raw_jobs"

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

    with open(config_path, "r") as f:
        sources = json.load(f)

    return sources
