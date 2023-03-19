class Enigma:

    def __init__(self, description, solution, hint):
        self.description = description
        self.solution = solution
        self.hint = hint

    def __repr__(self) -> str:
        return self.description + " - " + self.solution + " - " + self.hint
