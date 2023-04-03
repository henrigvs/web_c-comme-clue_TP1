from typing import List


from src.Riddles.api.service.dtos.CreateRiddleDTO import CreateRiddleDTO
from src.Riddles.api.service.dtos.RiddleDTO import RiddleDTO
from src.Riddles.api.service.mapper.RiddleMapper import RiddleMapper
from src.Riddles.domain.Riddle import Riddle


class RiddleService:
    def __init__(self, riddleRepository):
        self.riddleRepository = riddleRepository
        self.riddleMapper = RiddleMapper()

    # POST

    def addRiddle(self, createRiddleDTO: CreateRiddleDTO) -> RiddleDTO:
        riddle = self.riddleMapper.toEntity(createRiddleDTO)
        return self.riddleMapper.toDTO(self.riddleRepository.addRiddle(riddle))

    # DELETE

    def deleteRiddle(self, riddleId: str) -> RiddleDTO:
        return self.riddleMapper.toDTO(self.riddleRepository.deleteRiddle(riddleId))

    # PUT

    def updateRiddle(self, createRiddleDTO: CreateRiddleDTO, riddleId: str) -> RiddleDTO:
        riddle = Riddle(createRiddleDTO.description,
                        createRiddleDTO.solution,
                        createRiddleDTO.clue,
                        createRiddleDTO.difficulty)
        return self.riddleMapper.toDTO(self.riddleRepository.updateRiddle(riddle, riddleId))

    # GET

    def getAllRiddle(self) -> List[RiddleDTO]:
        return [self.riddleMapper.toDTO(riddle) for riddle in self.riddleRepository.getAllRiddle()]

    def getRiddleByID(self, riddleId: str) -> RiddleDTO:
        return self.riddleMapper.toDTO(self.riddleRepository.getRiddleByID(riddleId))
