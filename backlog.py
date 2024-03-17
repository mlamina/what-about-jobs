class Backlog:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def list_items(self):
        return self.items

    def reprioritize_item(self, item, new_priority):
        if item in self.items:
            self.items.remove(item)
            self.items.insert(new_priority, item)
