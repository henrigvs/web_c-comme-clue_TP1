from Enigmas.api.dtos.EnigmaDTO import EnigmaDTO
from Enigmas.domain.Enigma import Enigma


class EnigmaMapper:

    @staticmethod
    def toDTO(enigma):
        return EnigmaDTO(enigma.description, enigma.solution, enigma.hint)

    @staticmethod
    def toEntity(enigmaDTO):
        return Enigma(enigmaDTO.description, enigmaDTO.solution, enigmaDTO.hint)

