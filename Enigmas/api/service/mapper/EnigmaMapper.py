from Enigmas.api.service.dtos.EnigmaDTO import EnigmaDTO
from Enigmas.domain.Enigma import Enigma


class EnigmaMapper:

    @staticmethod
    def toDTO(enigma):
        if enigma is None:
            return None
        else:
            return EnigmaDTO(enigma.id, enigma.description, enigma.solution, enigma.hint, enigma.difficulty)

    @staticmethod
    def toEntity(createEnigmaDTO):
        return Enigma(createEnigmaDTO.description, createEnigmaDTO.solution, createEnigmaDTO.hint,
                      createEnigmaDTO.difficulty)

