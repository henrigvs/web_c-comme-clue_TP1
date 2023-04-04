class CreateRiddleDTO:

    def __init__(self, description, solution, clue, difficulty):
        self.description = description
        self.solution = solution
        self.clue = clue
        self.difficulty = difficulty
