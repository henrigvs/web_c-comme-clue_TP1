
class EnigmaRepository:

    def __init__(self):
        self.enigmas = []

    def addEnigma(self, enigma):
        self.enigmas.append(enigma)

    def getEnigmas(self):
        return self.enigmas

