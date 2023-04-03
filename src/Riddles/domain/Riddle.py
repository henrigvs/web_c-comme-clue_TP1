import uuid


class Riddle:

    def __init__(self, description: str, solution: str, clue: str, difficulty: int):
        self.riddleId = str(uuid.uuid4())
        self.description = description
        self.solution = solution
        self.clue = clue
        self.difficulty = difficulty

    def __repr__(self) -> str:
        return self.riddleId + " - " + self.description + " - " + self.solution + " - " + self.clue + " - " + str(
            self.difficulty)
