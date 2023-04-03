class RiddleDTO:

    def __init__(self, riddleId, description, solution, clue, difficulty):
        self.riddleId = riddleId
        self.description = description
        self.solution = solution
        self.clue = clue
        self.difficulty = difficulty

    def __eq__(self, other):
        if not isinstance(other, RiddleDTO):
            return False
        return (self.riddleId == other.riddleId and
                self.description == other.description and
                self.solution == other.solution and
                self.clue == other.clue and
                self.difficulty == other.difficulty)