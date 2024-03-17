import unittest
from backlog import Backlog

class TestBacklog(unittest.TestCase):
    def setUp(self):
        self.backlog = Backlog()

    def test_add_item(self):
        self.backlog.add_item('New item')
        self.assertIn('New item', self.backlog.items, "Item should be added to the backlog")

    def test_remove_item(self):
        self.backlog.add_item('Item to remove')
        self.backlog.remove_item('Item to remove')
        self.assertNotIn('Item to remove', self.backlog.items, "Item should be removed from the backlog")

    def test_list_items(self):
        self.backlog.add_item('Item 1')
        self.backlog.add_item('Item 2')
        items = self.backlog.list_items()
        self.assertEqual(items, ['Item 1', 'Item 2'], "Should list all items in the backlog")

    def test_reprioritize_item(self):
        self.backlog.add_item('Item 1')
        self.backlog.add_item('Item 2')
        self.backlog.reprioritize_item('Item 2', 0)
        items = self.backlog.list_items()
        self.assertEqual(items, ['Item 2', 'Item 1'], "Should reprioritize the item in the backlog")

if __name__ == '__main__':
    unittest.main()