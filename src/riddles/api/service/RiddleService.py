from typing import List

from src.riddles.api.service.dtos.CreateRiddleDTO import CreateRiddleDTO
from src.riddles.api.service.dtos.RiddleDTO import RiddleDTO
from src.riddles.api.service.mapper.RiddleMapper import RiddleMapper
from src.riddles.domain.Riddle import Riddle


class RiddleService:
    def __init__(self, riddleRepository):
        self.riddleRepository = riddleRepository
        self.riddleMapper = RiddleMapper()

    def addRiddle(self, createRiddleDTO: CreateRiddleDTO) -> RiddleDTO:
        riddle = self.riddleMapper.toEntity(createRiddleDTO)
        return self.riddleMapper.toDTO(self.riddleRepository.addRiddle(riddle))

    def deleteRiddle(self, riddleId: str) -> RiddleDTO:
        return self.riddleMapper.toDTO(self.riddleRepository.deleteRiddle(riddleId))

    def editRiddle(self, createRiddleDTO: CreateRiddleDTO, riddleId: str) -> RiddleDTO:
        riddle = Riddle(createRiddleDTO.description,
                        createRiddleDTO.solution,
                        createRiddleDTO.clue,
                        createRiddleDTO.difficulty)
        return self.riddleMapper.toDTO(self.riddleRepository.editRiddle(riddle, riddleId))

    def getAllRiddle(self) -> List[RiddleDTO]:
        return [self.riddleMapper.toDTO(riddle) for riddle in self.riddleRepository.getAllRiddle()]

    def getRiddleByID(self, riddleId: str) -> RiddleDTO:
        return self.riddleMapper.toDTO(self.riddleRepository.getRiddleByID(riddleId))
