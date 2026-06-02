import os
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

load_dotenv()

class DatabaseClient:
    def __init__(self):
        self.uri = os.getenv("MONGODB_URI")
        self.client = MongoClient(self.uri, server_api=ServerApi('1'))
        self.db = self.client["interactive_fiction"]
        self.collection = self.db["story_nodes"]

    def get_node_by_id(self, node_id: str):
        return self.collection.find_one({"node_id": node_id})

    def insert_nodes(self, nodes_data: list):
        if nodes_data:
            self.collection.insert_many(nodes_data)