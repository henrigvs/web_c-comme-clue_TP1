

class EnigmaRepository:

    def __init__(self):
        self.enigmas = {}

    def addEnigma(self, enigma):
        id = enigma.id
        self.enigmas[id] = enigma

    def updateEnigma(self, enigma, id):
        if id in self.enigmas:
            self.enigmas[id].description = enigma.description
            self.enigmas[id].solution = enigma.solution
            self.enigmas[id].hint = enigma.hint
            self.enigmas[id].difficulty = enigma.difficulty

    def getAllEnigmas(self):
        return self.enigmas.values()

    def getEnigmaByID(self, id):
        if id in self.enigmas:
            return self.enigmas[id]
        else:
            return None

    def deleteEnigma(self, id):
        if id in self.enigmas:
            self.enigmas.pop(id)

    def __repr__(self) -> str:
        stringBuilder = ""
        for element in self.enigmas.keys():
            stringBuilder += self.enigmas[element].description + " "
            stringBuilder += self.enigmas[element].solution + " "
            stringBuilder += self.enigmas[element].hint + "\n"
        return stringBuilder
