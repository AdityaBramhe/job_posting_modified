from pymongo import MongoClient

# Replace this with your actual MongoDB URI
MONGO_URI = "REMOVED<username>:<password>@jobposting.tgcylxz.mongodb.net/?retryWrites=true&w=majority"

try:
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)  # 5-second timeout
    db_names = client.list_database_names()  # Tries to connect
    print("✅ MongoDB connection successful.")
    print("Databases found:", db_names)
except Exception as e:
    print("❌ Failed to connect to MongoDB.")
    print("Error:", e)
