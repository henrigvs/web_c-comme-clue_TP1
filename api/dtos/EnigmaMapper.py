from api.dtos.EnigmaDTO import EnigmaDTO
from domain.Enigma import Enigma


class EnigmaMapper:

    @staticmethod
    def toDTO(enigma):
        return EnigmaDTO(enigma.id, enigma.description, enigma.solution)

    @staticmethod
    def toEntity(enigmaDTO):
        return Enigma(enigmaDTO.id, enigmaDTO.description, enigmaDTO.solution)

