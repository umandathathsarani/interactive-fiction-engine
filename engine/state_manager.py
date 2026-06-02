class StateManager:
    def __init__(self):
        self.inventory = []
        self.flags = {}
        self.current_node_id = "start"

    def add_item(self, item: str):
        if item not in self.inventory:
            self.inventory.append(item)

    def remove_item(self, item: str) -> bool:
        if item in self.inventory:
            self.inventory.remove(item)
            return True
        return False

    def has_item(self, item: str) -> bool:
        return item in self.inventory

    def set_flag(self, flag_name: str, value: bool):
        self.flags[flag_name] = value

    def get_flag(self, flag_name: str) -> bool:
        return self.flags.get(flag_name, False)

    def reset_state(self):
        self.inventory = []
        self.flags = {}
        self.current_node_id = "start"