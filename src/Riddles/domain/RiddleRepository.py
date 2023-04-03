from typing import List, Optional

from src.Riddles.domain.Riddle import Riddle


class RiddleRepository:

    def __init__(self):
        self.riddleRepository = {}

    def addRiddle(self, riddle: Riddle) -> Riddle:
        self.riddleRepository[riddle.riddleId] = riddle
        return riddle

    def updateRiddle(self, riddle: Riddle, riddleId: str) -> Riddle:
        if riddleId not in self.riddleRepository:
            return None

        self.riddleRepository[riddleId].description = riddle.description
        self.riddleRepository[riddleId].solution = riddle.solution
        self.riddleRepository[riddleId].clue = riddle.clue
        self.riddleRepository[riddleId].difficulty = riddle.difficulty

        return self.riddleRepository[riddleId]

    def getAllRiddle(self) -> List[Riddle]:
        return list(self.riddleRepository.values())

    def getRiddleByID(self, riddleId: str) -> Optional[Riddle]:
        return self.riddleRepository.get(riddleId)

    def deleteRiddle(self, riddleId: str) -> Riddle:
        riddleToBeDeleted = self.getRiddleByID(riddleId)
        if riddleToBeDeleted is not None:
            del self.riddleRepository[riddleId]
        return riddleToBeDeleted
