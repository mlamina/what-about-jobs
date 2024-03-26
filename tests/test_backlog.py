import pytest
from backlog import Backlog
import os


@pytest.fixture
def backlog_fixture():
    backlog = Backlog()
    yield backlog
    # Teardown code to remove any created files
    files = os.listdir('backlog/')
    for file in files:
        if file.endswith('.md'):
            os.remove(f'backlog/{file}')


def test_add_item(backlog_fixture):
    backlog_fixture.add_item(1, 'test-question', 'What is AI?')
    assert os.path.exists('backlog/1-test-question.md')


def test_remove_item(backlog_fixture):
    backlog_fixture.add_item(1, 'test-question', 'What is AI?')
    backlog_fixture.remove_item('test-question')
    assert not os.path.exists('backlog/1-test-question.md')


def test_reprioritize_item(backlog_fixture):
    backlog_fixture.add_item(1, 'test-question', 'What is AI?')
    backlog_fixture.reprioritize_item('test-question', 2)
    assert not os.path.exists('backlog/1-test-question.md')
    assert os.path.exists('backlog/2-test-question.md')


def test_pull_next_question(backlog_fixture):
    backlog_fixture.add_item(1, 'test-question', 'What is AI?')
    backlog_fixture.add_item(2, 'another-question', 'What is ML?')
    question = backlog_fixture.pull_next_question()
    assert question == 'What is AI?'