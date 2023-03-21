from Enigmas.api.dtos.EnigmaMapper import EnigmaMapper


class EnigmaService:
    def __init__(self, enigmaRepository):
        self.enigmaRepository = enigmaRepository

    # POST

    def addEnigma(self, enigmaDTO):
        self.enigmaRepository.addEnigma(EnigmaMapper.toEntity(enigmaDTO))



    # GET

    def getAllEnigmas(self):
        return [EnigmaMapper.toDTO(enigma) for enigma in self.enigmaRepository.getAllEnigmas()]

    def getEnigmaByID(self, id):
        return EnigmaMapper.toDTO(self.enigmaRepository.getEnigmaByID(id))
