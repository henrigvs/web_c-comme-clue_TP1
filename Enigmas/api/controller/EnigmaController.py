from Enigmas.api.dtos.EnigmaDTO import EnigmaDTO


class EnigmaController:

    def __init__(self, enigmaService):
        self.enigmaService = enigmaService

    # POST

    def addEnigma(self, description, solution, hint, difficulty):
        enigmaDTO = EnigmaDTO(description, solution, hint, difficulty)
        self.enigmaService.addEnigma(enigmaDTO)



    # GET

    def getAllEnigmas(self):
        enigmas = self.enigmaService.getAllEnigmas()
        return [
            {
                'description': enigma.description,
                'solution': enigma.solution,
                'hint': enigma.hint,
                'difficulty': enigma.difficulty
            }
                for enigma in enigmas]

    def getEnigmaById(self, id):
        enigma = self.enigmaService.getEnigmaByID(id)
        return \
            {
                'description': enigma.description,
                'solution': enigma.solution,
                'hint': enigma.hint,
                'difficulty': enigma.difficulty
            }
