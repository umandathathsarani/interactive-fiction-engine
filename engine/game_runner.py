import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.node import StoryNode
from integrations.db_client import DatabaseClient

def play_game():
    try:
        db_client = DatabaseClient()
    except ValueError as e:
        print(e)
        return

    current_node_id = "start"

    while current_node_id:
        raw_node = db_client.get_node_by_id(current_node_id)
        if not raw_node:
            print(f"\nError: Story node '{current_node_id}' not found in database.")
            break

        current_node = StoryNode(
            node_id=raw_node["node_id"],
            text=raw_node["text"],
            choices=raw_node.get("choices", [])
        )
        
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