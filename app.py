import os
import sys
from flask import Flask, render_template, request, jsonify

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from integrations.db_client import DatabaseClient
from engine.state_manager import StateManager
from integrations.ai_client import AIClient

app = Flask(__name__)

# Initialize our core engine components globally for the local server
try:
    db_client = DatabaseClient()
    state = StateManager()
    ai_client = AIClient()
except Exception as e:
    print(f"Startup Error: {e}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/state', methods=['GET'])
def get_state():
    raw_node = db_client.get_node_by_id(state.current_node_id)
    if not raw_node:
        return jsonify({"error": "Node not found"}), 404
        
    return jsonify({
        "text": raw_node["text"],
        "choices": raw_node.get("choices", []),
        "inventory": state.inventory
    })

@app.route('/api/choice', methods=['POST'])
def make_choice():
    data = request.json
    choice_idx = data.get('choice_idx')
    
    raw_node = db_client.get_node_by_id(state.current_node_id)
    choices = raw_node.get("choices", [])
    
    if 0 <= choice_idx < len(choices):
        chosen = choices[choice_idx]
        
        # Check requirements
        if "required_item" in chosen and not state.has_item(chosen["required_item"]):
            return jsonify({"status": "locked", "message": f"You need the {chosen['required_item']}."})
            
        # Add items
        if "add_item" in chosen:
            state.add_item(chosen["add_item"])
            
        # Move to next node
        state.current_node_id = chosen["next_node"]
        return jsonify({"status": "success"})
        
    return jsonify({"error": "Invalid choice"}), 400

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data.get('text')
    
    raw_node = db_client.get_node_by_id(state.current_node_id)
    ai_response = ai_client.generate_npc_response(raw_node["text"], user_input)
    
    return jsonify({"response": ai_response})

# Resets the game state back to the start
@app.route('/api/reset', methods=['POST'])
def reset_game():
    state.reset_state()
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)