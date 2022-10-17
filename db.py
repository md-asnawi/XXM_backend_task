from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')

conn = MongoClient(f"mongodb+srv://{DB_USERNAME}:{DB_PASSWORD}@xxm-cluster.ow4ljlw.mongodb.net/?retryWrites=true&w=majority")
db = conn.XXM
collection = db.pallet