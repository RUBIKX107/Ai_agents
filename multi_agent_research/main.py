from agents.orchestrator import OrchestratorAgent


def main():

    question = input("Enter research question: ")

    orchestrator = OrchestratorAgent()

    report = orchestrator.run(question)

    print(report)


if __name__ == "__main__":
    main()