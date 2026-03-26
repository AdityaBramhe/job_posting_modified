from pymongo import MongoClient
from datetime import datetime

MONGO_URI = "REMOVEDadityabramhe7:<C3kg0TDi21QaKOAM>@cluster0.is9smo4.mongodb.net/"

client = MongoClient(MONGO_URI)
db = client["JobPosting"]
collection = db["ProcessedSignals"]

sample_data = [
    {
        "company": "Amazon",
        "department": "Engineering",
        "description": "urgent hiring for backend engineer with python aws",
        "tech_stack": ["Python", "AWS"],
        "posting_date": datetime.now()
    },
    {
        "company": "Google",
        "department": "AI",
        "description": "immediate requirement for ML engineer tensorflow",
        "tech_stack": ["ML", "TensorFlow"],
        "posting_date": datetime.now()
    },
    {
        "company": "Microsoft",
        "department": "Cloud",
        "description": "looking for cloud engineer azure",
        "tech_stack": ["Azure", "Cloud"],
        "posting_date": datetime.now()
    },
    {
        "company": "Flipkart",
        "department": "Data",
        "description": "urgent data analyst sql python",
        "tech_stack": ["SQL", "Python"],
        "posting_date": datetime.now()
    }
]

collection.insert_many(sample_data)

print("✅ Sample data inserted!")