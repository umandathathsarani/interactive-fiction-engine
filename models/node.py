class StoryNode:
    def __init__(self, node_id: str, text: str, choices: list):
        self.node_id = node_id
        self.text = text
        self.choices = choices

    def display(self):
        print(f"\n--- {self.node_id.upper()} ---") 
        print(self.text)
        print("\nWhat do you do?")
        
        for index, choice in enumerate(self.choices):
            print(f"{index + 1}. {choice['choice_text']}")