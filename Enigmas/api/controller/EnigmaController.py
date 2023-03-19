from Enigmas.api.dtos.EnigmaDTO import EnigmaDTO


class EnigmaController:

    def __init__(self, enigmaService):
        self.enigmaService = enigmaService

    def addEnigma(self, description, solution, hint):
        enigmaDTO = EnigmaDTO(description, solution, hint)
        self.enigmaService.addEnigma(enigmaDTO)

    def getAllEnigmas(self):
        enigmas = self.enigmaService.getAllEnigmas()
        return [{'description': enigma.description,
                 'solution': enigma.solution,
                 'hint': enigma.hint}
                for enigma in enigmas]

    def getEnigmaById(self, id):
        enigma = self.enigmaService.getEnigmaByID(id)
        return {'description': enigma.description,
                'solution': enigma.solution,
                'hint': enigma.hint}
