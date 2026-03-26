# mongo_loader.py

import pandas as pd
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

import os

MONGO_URI = os.getenv("MONGO_URI")


def load_data():
    client = MongoClient(MONGO_URL)

    # ✅ FIXED DB + COLLECTION
    db = client["job_posting_modified"]
    collection = db["job_signals"]

    data = list(collection.find())

    if not data:
        print("⚠️ No data found in job_signals")
        return pd.DataFrame()

    df = pd.DataFrame(data)

    # clean Mongo _id
    if "_id" in df.columns:
        df.drop(columns=["_id"], inplace=True)

    return df