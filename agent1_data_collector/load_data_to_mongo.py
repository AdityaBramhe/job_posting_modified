import os
import pandas as pd
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get MongoDB URI and Database Name from environment variables
MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = os.getenv("MONGO_DATABASE", "job_intel_db")  # default if not set
COLLECTION_NAME = os.getenv("MONGO_COLLECTION", "ds_salary_data")

# Path to the downloaded CSV (KaggleHub default)
CSV_PATH = os.path.expanduser("~/.cache/kagglehub/datasets/ruchi798/data-science-job-salaries/versions/1/ds_salaries.csv")

# Load the dataset
df = pd.read_csv(CSV_PATH)

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]

# Clear existing records to avoid duplicates
collection.delete_many({})

# Insert new records
records = df.to_dict(orient='records')
collection.insert_many(records)

# Print summary
print("✅ Data inserted into MongoDB successfully!")
print(f"📊 Total records inserted: {len(records)}")
