import os
import json
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dotenv_path = os.path.join(base_dir, '.env')
load_dotenv(dotenv_path)

class DatabaseClient:
    def __init__(self):
        self.uri = os.getenv("MONGODB_URI")
        if not self.uri:
            raise ValueError("Critical Error: MONGODB_URI not found in environment variables!")
        
        self.client = MongoClient(self.uri, server_api=ServerApi('1'))
        self.db = self.client["interactive_fiction"]
        self.collection = self.db["story_nodes"]

    def get_node_by_id(self, node_id: str):
        return self.collection.find_one({"node_id": node_id})

    def insert_nodes(self, nodes_data: list):
        if nodes_data:
            self.collection.insert_many(nodes_data)

if __name__ == "__main__":
    try:
        client = DatabaseClient()
        
        json_path = os.path.join(base_dir, "data", "story_nodes.json")
        
        with open(json_path, 'r') as file:
            raw_story = json.load(file)
        
        nodes_list = list(raw_story.values())
        
        client.collection.delete_many({})
        client.insert_nodes(nodes_list)
        print("Story nodes successfully uploaded to MongoDB Atlas!")
        
    except Exception as e:
        print(f"An error occurred: {e}")