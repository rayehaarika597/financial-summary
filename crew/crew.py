from crewai import Crew, Agent, Task

import yaml
from pathlib import Path

from crew.models.summary_model import DocumentSummary


def document_summary(document: str):
    try:
        path = Path(r'crew/financial_summary.yaml')
        yaml_path = path.resolve()

        with yaml_path.open() as file:
            config = yaml.safe_load(file)

        agents_config = config['agents']
        tasks_config = config['tasks']

        extractor = Agent(
            config=agents_config['extractor']
        )

        summarizer = Agent(
            config=agents_config['summarizer']
        )

        proofreader = Agent(
            config=agents_config['proofreader']
        )

        extraction = Task(
            config=tasks_config['extraction'],
            agent=extractor,
            output_pydantic=DocumentSummary
        )

        summarization = Task(
            config=tasks_config['summarization'],
            agent=summarizer,
            output_pydantic=DocumentSummary
        )

        proofreading = Task(
            config=tasks_config['proofreading'],
            agent=proofreader,
            output_pydantic=DocumentSummary
        )

        crew = Crew(
            tasks=[extraction, summarization, proofreading],
            agents=[extractor, summarizer, proofreader],
            memory=True
        )

        result = crew.kickoff(
            inputs={
                'document': document
            }
        )

        return result.pydantic.summary
    except Exception as e:
        print("Error", e)
