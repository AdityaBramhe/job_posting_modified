import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# =========================
# MongoDB Configuration
# =========================
MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME", "job_posting_modified")
RAW_JOBS_COLLECTION = "raw_jobs"

if not MONGO_URI:
    raise ValueError("MONGO_URI not set in environment variables")

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