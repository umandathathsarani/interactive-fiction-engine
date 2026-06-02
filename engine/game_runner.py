import json
import os

def load_story_data(filepath: str) -> dict:
    """
    Loads the story nodes from a JSON file.
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    full_path = os.path.join(base_dir, filepath)

    try:
        with open(full_path, 'r') as file:
            data = json.load(file)
            print("Story data loaded successfully!")
            return data
    except FileNotFoundError:
        print(f"Error: Could not find story file at {full_path}")
        return {}

if __name__ == "__main__":
    story_data = load_story_data("data/story_nodes.json")