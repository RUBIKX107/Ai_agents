from ddgs import DDGS
from agents.base_agent import BaseAgent


class SearchAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            name="SearchAgent",
            role="Searches the web"
        )

    def process(self, message):

        query = message.payload

        results = []

        with DDGS() as ddgs:
            search_results = ddgs.text(query, max_results=5)

            for r in search_results:
                results.append({
                    "title": r["title"],
                    "body": r["body"],
                    "link": r["href"]
                })

        return results