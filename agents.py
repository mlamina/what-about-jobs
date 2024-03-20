"""
This module implements the Crew AI agent system for the 'What About Jobs?' project.

It defines agents with specific roles to handle tasks such as pulling questions from the backlog,
planning and executing research, and writing findings into Markdown files.
"""

from langchain.agents import Agent
from backlog import Backlog

# Define the roles for our agents
ROLES = ['BacklogPuller', 'ResearchPlanner', 'ResearchExecutor', 'MarkdownWriter']


class BacklogPuller(Agent):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.role = 'BacklogPuller'
        self.backlog = Backlog()

    def pull_question(self):
        # Implementation for pulling a question from the backlog
        return self.backlog.pull_next_question()


class ResearchPlanner(Agent):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.role = 'ResearchPlanner'

    def plan_research(self, question):
        # Implementation for creating a research plan based on a question
        print(f"Planning research for: {question}")


class ResearchExecutor(Agent):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.role = 'ResearchExecutor'

    def execute_research(self, plan):
        # Implementation for executing the research based on a plan
        print(f"Executing research plan: {plan}")


class MarkdownWriter(Agent):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.role = 'MarkdownWriter'

    def write_findings(self, findings):
        # Implementation for writing findings into Markdown files
        print(f"Writing findings: {findings}")

# Initialize agents
agents = {
    role: globals()[role]() for role in ROLES
}
