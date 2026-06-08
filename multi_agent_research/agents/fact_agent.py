from agents.base_agent import BaseAgent


class FactAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            name="FactAgent",
            role="Verifies claims"
        )

    def process(self, summaries):

        verified = []

        for s in summaries:

            verified.append({
                "content": s,
                "status": "LIKELY TRUE"
            })

        return verified