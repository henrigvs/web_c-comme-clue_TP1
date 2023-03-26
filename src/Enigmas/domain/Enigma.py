import uuid


class Enigma:

    def __init__(self, description, solution, hint, difficulty):
        self.id = str(uuid.uuid4())
        self.description = description
        self.solution = solution
        self.hint = hint
        self.difficulty = difficulty

    def __repr__(self) -> str:
        return self.id + " - " + self.description + " - " + self.solution + " - " + self.hint + " - " + self.difficulty
