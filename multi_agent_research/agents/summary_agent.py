from agents.base_agent import BaseAgent


class SummaryAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            name="SummaryAgent",
            role="Summarizes research"
        )

    def process(self, search_results):

        summaries = []

        for result in search_results:

            summary = f"""
TITLE:
{result['title']}

SUMMARY:
{result['body']}
"""

            summaries.append(summary)

        return summaries