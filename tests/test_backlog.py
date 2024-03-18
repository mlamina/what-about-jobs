import pytest
from backlog import Backlog
import os


def test_add_item():
    backlog = Backlog()
    backlog.add_item(1, 'test-question', 'What is AI?')
    assert os.path.exists('backlog/1-test-question.md')
    os.remove('backlog/1-test-question.md')


def test_remove_item():
    backlog = Backlog()
    backlog.add_item(1, 'test-question', 'What is AI?')
    backlog.remove_item('test-question')
    assert not os.path.exists('backlog/1-test-question.md')


def test_reprioritize_item():
    backlog = Backlog()
    backlog.add_item(1, 'test-question', 'What is AI?')
    backlog.reprioritize_item('test-question', 2)
    assert not os.path.exists('backlog/1-test-question.md')
    assert os.path.exists('backlog/2-test-question.md')
    os.remove('backlog/2-test-question.md')


def test_pull_next_question():
    backlog = Backlog()
    backlog.add_item(1, 'test-question', 'What is AI?')
    backlog.add_item(2, 'another-question', 'What is ML?')
    question = backlog.pull_next_question()
    assert question == 'What is AI?'
    os.remove('backlog/1-test-question.md')
    os.remove('backlog/2-another-question.md')