import uuid


class Riddle:

    def __init__(self, description: str, solution: str, clue: str, difficulty: int, ownerId: str):
        self.riddleId = str(uuid.uuid4())
        self.description = description
        self.solution = solution
        self.clue = clue
        self.difficulty = difficulty
        self.ownerId = ownerId

    def __repr__(self) -> str:
        return self.riddleId + " - " + self.description + " - " + self.solution + " - " + self.clue + " - " + str(
            self.difficulty) + " - " + self.ownerId
