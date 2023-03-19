

class EnigmaRepository:

    def __init__(self):
        self.enigmas = {}

    def addEnigma(self, enigma):
        size = len(self.enigmas)
        self.enigmas[size + 1] = enigma

    def getAllEnigmas(self):
        return self.enigmas.values()

    def getEnigmaByID(self, myKey):
        if myKey in self.enigmas:
            return self.enigmas[myKey]
        else:
            return None

    def __repr__(self) -> str:
        stringBuilder = ""
        for element in self.enigmas.keys():
            stringBuilder += self.enigmas[element].description + " "
            stringBuilder += self.enigmas[element].solution + " "
            stringBuilder += self.enigmas[element].hint + "\n"
        return stringBuilder
