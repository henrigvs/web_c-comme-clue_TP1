from src.Riddles.api.service.dtos.RiddleDTO import RiddleDTO
from src.Riddles.domain.Riddle import Riddle


class RiddleMapper:

    @staticmethod
    def toDTO(riddle):
        if riddle is None:
            return None
        else:
            return RiddleDTO(riddle.riddleId, riddle.description, riddle.solution, riddle.clue, riddle.difficulty)

    @staticmethod
    def toEntity(createRiddleDTO):
        return Riddle(createRiddleDTO.description,
                      createRiddleDTO.solution,
                      createRiddleDTO.clue,
                      createRiddleDTO.difficulty)

