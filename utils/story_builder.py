import os
import sys
import json

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
json_path = os.path.join(base_dir, 'data', 'story_nodes.json')

def load_local_story():
    if os.path.exists(json_path):
        with open(json_path, 'r') as f:
            return json.load(f)
    return {}

def save_local_story(data):
    with open(json_path, 'w') as f:
        json.dump(data, f, indent=2)

def main():
    print("\n")
    print("   INTERACTIVE STORY BUILDER CLI     ")
    print("\n")
    
    story_data = load_local_story()
    
    node_id = input("Enter unique Node ID (e.g., hidden_vault): ").strip().lower()
    if not node_id:
        print("Error: Node ID cannot be empty.")
        return
        
    if node_id in story_data:
        overwrite = input(f"Node '{node_id}' already exists. Overwrite? (y/n): ").strip().lower()
        if overwrite != 'y':
            return

    text = input("Enter the scene description text:\n> ").strip()
    
    choices = []
    print("\n--- Add Choices (Leave choice text blank to finish) ---")
    while True:
        choice_text = input(f"\nChoice {len(choices) + 1} Text: ").strip()
        if not choice_text:
            break
            
        next_node = input("Destination Node ID when chosen: ").strip().lower()
        req_item = input("Required item to unlock (Leave blank for none): ").strip()
        add_item = input("Item awarded by choosing this (Leave blank for none): ").strip()
        
        choice_obj = {
            "choice_text": choice_text,
            "next_node": next_node
        }
        if req_item:
            choice_obj["required_item"] = req_item
        if add_item:
            choice_obj["add_item"] = add_item
            
        choices.append(choice_obj)

    story_data[node_id] = {
        "node_id": node_id,
        "text": text,
        "choices": choices
    }
    
    save_local_story(story_data)
    print(f"\n🎉 Success! '{node_id}' written safely to data/story_nodes.json.")
    print("Run 'python integrations/db_client.py' to push your changes live to Atlas.")

if __name__ == "__main__":
    main()