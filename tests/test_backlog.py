import unittest
from backlog import Backlog
import os


class TestBacklog(unittest.TestCase):
    def setUp(self):
        self.backlog = Backlog()
        # Clean up the backlog directory before each test
        for filename in os.listdir('backlog/'):
            os.remove(os.path.join('backlog/', filename))

    def test_add_item(self):
        self.backlog.add_item(1, 'test-question', 'What is AI?')
        self.assertTrue(os.path.exists('backlog/1-test-question.md'))

    def test_remove_item(self):
        self.backlog.add_item(1, 'test-question', 'What is AI?')
        self.backlog.remove_item('test-question')
        self.assertFalse(os.path.exists('backlog/1-test-question.md'))

    def test_reprioritize_item(self):
        self.backlog.add_item(1, 'test-question', 'What is AI?')
        self.backlog.reprioritize_item('test-question', 2)
        self.assertFalse(os.path.exists('backlog/1-test-question.md'))
        self.assertTrue(os.path.exists('backlog/2-test-question.md'))

    def test_pull_next_question(self):
        self.backlog.add_item(1, 'test-question', 'What is AI?')
        self.backlog.add_item(2, 'another-question', 'What is ML?')
        question = self.backlog.pull_next_question()
        self.assertEqual(question, 'What is AI?')

if __name__ == '__main__':
    unittest.main()
