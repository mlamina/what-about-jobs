class Backlog:
    """
    A class to manage backlog items with functionalities to add, remove, list, and reprioritize items.
    """
    def __init__(self):
        """
        Initializes the Backlog with an empty list of items.
        """
        self.items = []
        self._populate_backlog_from_files()

    def _populate_backlog_from_files(self):
        """
        Populates the backlog items from files in the backlog directory.
        """
        import glob
        backlog_files = glob.glob('backlog/*.md')
        for file_path in backlog_files:
            priority, question_slug = file_path.split('/')[-1].split('-')
            with open(file_path, 'r') as file:
                question = file.read().strip()
            self.items.append((int(priority), question_slug, question))

    def add_item(self, item):
        """
        Adds an item to the backlog.

        :param item: The item to be added to the backlog.
        """
        self.items.append(item)

    def remove_item(self, item):
        """
        Removes an item from the backlog if it exists.

        :param item: The item to be removed from the backlog.
        """
        if item in self.items:
            self.items.remove(item)

    def list_items(self):
        """
        Lists all items in the backlog.

        :return: A list of all items in the backlog.
        """
        return self.items

    def reprioritize_item(self, item, new_priority):
        """
        Reprioritizes an item in the backlog.

        :param item: The item to be reprioritized.
        :param new_priority: The new priority index for the item.
        """
        if item in self.items:
            index = self.items.index(item)
            self.items.remove(item)
            self.items.insert(new_priority, item)

    def pull_next_question(self):
        """
        Finds and returns the item with the highest priority.

        :return: The item with the highest priority.
        """
        if not self.items:
            return None
        highest_priority_item = min(self.items, key=lambda item: item[0])
        self.items.remove(highest_priority_item)
        return highest_priority_item[2]
