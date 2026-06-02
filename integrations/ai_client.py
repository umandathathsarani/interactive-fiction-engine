import os
from google import genai
from dotenv import load_dotenv

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dotenv_path = os.path.join(base_dir, '.env')
load_dotenv(dotenv_path)

class AIClient:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("Critical Error: GEMINI_API_KEY not found in environment variables!")
        
        self.client = genai.Client(api_key=api_key)
        self.model_name = 'gemini-2.5-flash'

    def generate_npc_response(self, context: str, player_input: str) -> str:
        prompt = f"Context: {context}\nPlayer says: {player_input}\nRespond as an NPC or narrator in character, keeping it concise (1-2 sentences)."
        try:
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=prompt
            )
            return response.text.strip()
        except Exception as e:
            return f"Error generating response: {e}"