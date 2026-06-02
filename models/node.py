class StoryNode:
    def __init__(self, node_id: str, text: str, choices: list):
        """
        Initializes a single scene in the interactive fiction engine.
        
        :param node_id: A unique identifier for this scene (e.g., "intro_01")
        :param text: The actual story text the user will read.
        :param choices: A list of dictionaries representing the user's options.
        """
        self.node_id = node_id
        self.text = text
        self.choices = choices

    def display(self):
        """Prints the story text and the available choices to the terminal."""
        print(f"\n--- {self.node_id.upper()} ---") 
        print(self.text)
        print("\nWhat do you do?")
        
        for index, choice in enumerate(self.choices):
            print(f"{index + 1}. {choice['choice_text']}")