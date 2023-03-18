from api.dtos.EnigmaMapper import EnigmaMapper


class EnigmaService:
    def __init__(self, enigmaRepository):
        self.enigmaRepository = enigmaRepository

    def addEnigma(self, enigmaDTO):
        enigma = EnigmaMapper.toEntity(enigmaDTO)
        self.enigmaRepository.addEnigma(enigma)

    def getAllEnigmas(self):
        enigmas = self.enigmaRepository.getEnigmas()
        return [EnigmaMapper.toDTO(enigma) for enigma in enigmas]

