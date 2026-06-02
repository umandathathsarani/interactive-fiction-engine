import json
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.node import StoryNode

def load_story_data(filepath: str) -> dict:
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    full_path = os.path.join(base_dir, filepath)
    
    try:
        with open(full_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: Could not find story file at {full_path}")
        return {}

def play_game():
    raw_data = load_story_data("data/story_nodes.json")
    if not raw_data:
        return

    story_nodes = {}
    for key, value in raw_data.items():
        story_nodes[key] = StoryNode(
            node_id=value["node_id"],
            text=value["text"],
            choices=value.get("choices", [])
        )

    current_node_id = "start"

    while current_node_id in story_nodes:
        current_node = story_nodes[current_node_id]
        current_node.display()

        if not current_node.choices:
            print("\n--- THE END ---")
            break

        user_input = input("\nEnter your choice: ")
        
        try:
            choice_idx = int(user_input) - 1
            if 0 <= choice_idx < len(current_node.choices):
                current_node_id = current_node.choices[choice_idx]["next_node"]
            else:
                print("\nInvalid choice. Please pick a valid number.")
        except ValueError:
            print("\nInvalid input. Please enter a number.")

if __name__ == "__main__":
    play_game()