from pymongo import MongoClient

MONGO_URI = "REMOVEDadityabramhe7:YOUR_PASSWORD@cluster0.is9smo4.mongodb.net/"

try:
    client = MongoClient(MONGO_URI)
    db = client["JobPosting"]
    print("✅ Connected to MongoDB!")
except Exception as e:
    print("❌ Error:", e)