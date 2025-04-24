from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
client = MongoClient(os.getenv("MONGO_URI"))
db = client["furia_bot"]
users = db["users"]

def add_user(user_id, name):
    users.update_one(
        {"user_id": user_id},
        {"$set": {"name": name}},
        upsert=True
    )
