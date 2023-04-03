from src.Riddles.api.service.mapper.EnigmaMapper import EnigmaMapper


class RiddleService:
    def __init__(self, enigmaRepository):
        self.enigmaRepository = enigmaRepository

    # POST

    def addEnigma(self, createEnigmaDTO):
        self.enigmaRepository.addEnigma(EnigmaMapper.toEntity(createEnigmaDTO))

    # DELETE

    def deleteEnigma(self, id):
        self.enigmaRepository.deleteEnigma(id)

    # PUT

    def updateEnigma(self, enigmaDTO, id):
        self.enigmaRepository.updateEnigma(EnigmaMapper.toEntity(enigmaDTO), id)

    # GET

    def getAllEnigmas(self):
        return [EnigmaMapper.toDTO(enigma) for enigma in self.enigmaRepository.getAllEnigmas()]

    def getEnigmaByID(self, id):
        return EnigmaMapper.toDTO(self.enigmaRepository.getEnigmaByID(id))
