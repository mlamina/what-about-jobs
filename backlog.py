import glob
import os

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
        backlog_files = glob.glob('backlog/*.md')
        for file_path in backlog_files:
            parts = file_path.split('/')[-1].split('-', 1)
            if len(parts) == 2:
                priority, question_slug = parts
                with open(file_path, 'r') as file:
                    question = file.read().strip()
                self.items.append((int(priority), question_slug, question))

    def add_item(self, priority, question_slug, question):
        """
        Adds an item to the backlog by creating a new file.

        :param priority: The priority of the item.
        :param question_slug: The slug for the question.
        :param question: The question text.
        """
        file_name = f'backlog/{priority}-{question_slug}.md'
        with open(file_name, 'w') as file:
            file.write(question)
        self._populate_backlog_from_files()

    def remove_item(self, question_slug):
        """
        Removes an item from the backlog by deleting its file.

        :param question_slug: The slug of the question to be removed.
        """
        for priority, slug, question in self.items:
            if slug == question_slug:
                os.remove(f'backlog/{priority}-{slug}.md')
                break
        self._populate_backlog_from_files()

    def reprioritize_item(self, question_slug, new_priority):
        """
        Reprioritizes an item in the backlog by renaming its file.

        :param question_slug: The slug of the question to be reprioritized.
        :param new_priority: The new priority index for the item.
        """
        for priority, slug, question in self.items:
            if slug == question_slug:
                os.rename(f'backlog/{priority}-{slug}.md', f'backlog/{new_priority}-{slug}.md')
                break
        self._populate_backlog_from_files()

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
