from agents.base_agent import BaseAgent


class WriterAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            name="WriterAgent",
            role="Writes final report"
        )

    def process(self, verified_results):

        report = "\n\n===== FINAL REPORT =====\n\n"

        for item in verified_results:

            report += item["content"]
            report += f"\nFACT CHECK: {item['status']}\n\n"

        return report