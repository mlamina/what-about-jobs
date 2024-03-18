import pytest
from backlog import Backlog


class TestBacklog:
    @pytest.fixture
    def backlog(self):
        return Backlog()

    def test_add_item(self, backlog):
        backlog.add_item((1, 'test_slug', 'Test question?'))
        assert (1, 'test_slug', 'Test question?') in backlog.items

    def test_remove_item(self, backlog):
        item = (1, 'test_slug', 'Test question?')
        backlog.add_item(item)
        backlog.remove_item(item)
        assert item not in backlog.items

    def test_list_items(self, backlog):
        backlog.add_item((1, 'test_slug', 'Test question?'))
        assert backlog.list_items() == [(1, 'test_slug', 'Test question?')]

    def test_reprioritize_item(self, backlog):
        item = (1, 'test_slug', 'Test question?')
        backlog.add_item(item)
        backlog.reprioritize_item(item, 0)
        assert backlog.items[0] == item

    def test_pull_next_question(self, backlog):
        backlog.add_item((2, 'test_slug_2', 'Test question 2?'))
        backlog.add_item((1, 'test_slug_1', 'Test question 1?'))
        assert backlog.pull_next_question() == 'Test question 1?'
