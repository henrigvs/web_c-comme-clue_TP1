from api.dtos.EnigmaDTO import EnigmaDTO


class EnigmaController:

    def __init__(self, enigmaService):
        self.enigmaService = enigmaService

    def addEnigma(self, id, description, solution):
        enigmaDTO = EnigmaDTO(id, description, solution)
        self.enigmaService.addEnigma(enigmaDTO)

    def getAllEnigmas(self):
        enigmas = self.enigmaService.getAllEnigmas()
        return [{'id': enigma.id,
                 'description': enigma.description,
                 'solution': enigma.solution}
                for enigma in enigmas]

