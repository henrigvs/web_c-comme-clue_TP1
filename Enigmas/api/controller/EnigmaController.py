from Enigmas.api.service.dtos.CreateEnigmaDTO import CreateEnigmaDTO
from Enigmas.api.service.dtos.EnigmaDTO import EnigmaDTO


class EnigmaController:

    def __init__(self, enigmaService):
        self.enigmaService = enigmaService

    # POST

    def addEnigma(self, description, solution, hint, difficulty):
        createEnigmaDTO = CreateEnigmaDTO(description, solution, hint, difficulty)
        self.enigmaService.addEnigma(createEnigmaDTO)

    # PUT

    def updateEnigma(self, id, description, solution, hint, difficulty):
        enigmaDTO = EnigmaDTO(id, description, solution, hint, difficulty)
        self.enigmaService.updateEnigma(enigmaDTO)

    # DELETE
    def deleteEnigma(self, id):
        self.enigmaService.deleteEnigma(id)

    # GET

    def getAllEnigmas(self):
        enigmas = self.enigmaService.getAllEnigmas()
        json = []
        for enigma in enigmas:
            json.append({
                    'id': str(enigma.id),
                    'description': enigma.description,
                    'solution': enigma.solution,
                    'hint': enigma.hint,
                    'difficulty': enigma.difficulty
                    })
        return json

    def getEnigmaById(self, id):
        enigma = self.enigmaService.getEnigmaByID(id)
        return {
                'id': enigma.id,
                'description': enigma.description,
                'solution': enigma.solution,
                'hint': enigma.hint,
                'difficulty': enigma.difficulty
                }
