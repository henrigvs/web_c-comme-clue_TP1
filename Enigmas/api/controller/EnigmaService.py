from Enigmas.api.dtos.EnigmaMapper import EnigmaMapper


class EnigmaService:
    def __init__(self, enigmaRepository):
        self.enigmaRepository = enigmaRepository

    def addEnigma(self, enigmaDTO):
        self.enigmaRepository.addEnigma(EnigmaMapper.toEntity(enigmaDTO))

    def getAllEnigmas(self):
        return [EnigmaMapper.toDTO(enigma) for enigma in self.enigmaRepository.getAllEnigmas()]

    def getEnigmaByID(self, id):
        return self.enigmaRepository.getEnigmaByID(id)
