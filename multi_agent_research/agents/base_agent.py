class BaseAgent:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def process(self, message):
        raise NotImplementedError