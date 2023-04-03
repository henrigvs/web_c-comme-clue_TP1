from src.Riddles.api.service.dtos.EnigmaDTO import EnigmaDTO
from src.Riddles.domain.Riddle import Riddle


class EnigmaMapper:

    @staticmethod
    def toDTO(enigma):
        if enigma is None:
            return None
        else:
            return EnigmaDTO(enigma.riddleId, enigma.description, enigma.solution, enigma.hint, enigma.difficulty)

    @staticmethod
    def toEntity(createEnigmaDTO):
        return Riddle(createEnigmaDTO.description, createEnigmaDTO.solution, createEnigmaDTO.hint,
                      createEnigmaDTO.difficulty)

