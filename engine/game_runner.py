import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.node import StoryNode
from integrations.db_client import DatabaseClient
from engine.state_manager import StateManager
from integrations.ai_client import AIClient

def play_game():
    try:
        db_client = DatabaseClient()
        state = StateManager()
        ai_client = AIClient()
    except ValueError as e:
        print(e)
        return

    while state.current_node_id:
        raw_node = db_client.get_node_by_id(state.current_node_id)
        if not raw_node:
            print(f"\nError: Story node '{state.current_node_id}' not found in database.")
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

        user_input = input("\nEnter choice, 'i' for inventory, or speak to the narrator: ").strip()
        
        if not user_input:
            continue

        if user_input.lower() == 'i':
            print(f"\nInventory: {', '.join(state.inventory) if state.inventory else 'Empty'}")
            continue

        try:
            choice_idx = int(user_input) - 1
            if 0 <= choice_idx < len(current_node.choices):
                chosen_choice = current_node.choices[choice_idx]
                
                if "required_item" in chosen_choice and not state.has_item(chosen_choice["required_item"]):
                    print(f"\n🔒 Locked: You need the '{chosen_choice['required_item']}' to choose this option.")
                    continue
                
                if "add_item" in chosen_choice:
                    state.add_item(chosen_choice["add_item"])
                    print(f"\n[!] Item acquired: {chosen_choice['add_item']}")

                state.current_node_id = chosen_choice["next_node"]
            else:
                print("\nInvalid choice. Please pick a valid number.")
        except ValueError:
            print("\n[Analyzing your words...]")
            ai_response = ai_client.generate_npc_response(
                context=current_node.text, 
                player_input=user_input
            )
            print(f"\n🤖 Narrator: {ai_response}")

if __name__ == "__main__":
    play_game()