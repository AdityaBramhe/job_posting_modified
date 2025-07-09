import pandas as pd
from pymongo import MongoClient


def load_data(limit=16):
    client = MongoClient("REMOVEDadityabramhe7:C3kg0TDi21QaKOAM@jobposting.tgcylyz.mongodb.net/")
    db = client["JobPosting"]  # ✅ Must match what you used in Agent 2
    collection = db["ProcessedSignals"]  # ✅ Should be the same collection Agent 2 inserts into

    data = list(collection.find().sort([("_id", -1)]).limit(limit))
    df = pd.DataFrame(data)

    print(f"✅ Loaded {len(df)} job posts from MongoDB.")
    return df

