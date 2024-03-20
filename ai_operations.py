"""
This module utilizes the `langchain` library to perform AI operations. It is responsible for generating new content,
analyzing data, or any other AI-driven task relevant to the project.
"""

from agents import agents

def execute_ai_operations() -> None:
    """Execute AI operations using langchain and the agent crew."""
    for role, agent in agents.items():
        if role == 'BacklogPuller':
            question = agent.pull_question()
            print(f"Pulled question: {question}")
        elif role == 'ResearchPlanner':
            plan = agent.plan_research(question)
            print(f"Created plan for: {question}")
        elif role == 'ResearchExecutor':
            findings = agent.execute_research(plan)
            print(f"Executed research for: {plan}")
        elif role == 'MarkdownWriter':
            agent.write_findings(findings)
            print(f"Wrote findings into Markdown file")
