from protocols.a2a import AgentMessage

from agents.search_agent import SearchAgent
from agents.summary_agent import SummaryAgent
from agents.fact_agent import FactAgent
from agents.writer_agent import WriterAgent


class OrchestratorAgent:

    def __init__(self):

        self.search_agent = SearchAgent()
        self.summary_agent = SummaryAgent()
        self.fact_agent = FactAgent()
        self.writer_agent = WriterAgent()

    def run(self, question):

        print("\n[ORCHESTRATOR] Starting research...\n")

        search_message = AgentMessage(
            sender="Orchestrator",
            receiver="SearchAgent",
            task="search",
            payload=question
        )

        search_results = self.search_agent.process(search_message)

        summaries = self.summary_agent.process(search_results)

        verified = self.fact_agent.process(summaries)

        final_report = self.writer_agent.process(verified)

        return final_report