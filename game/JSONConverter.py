class JSONConverter:

    @staticmethod
    def getEnigmasFromJSON(jsonData):
        enigmas = []
        for data in jsonData:
            enigma = {
                "description": data["description"],
                "hint": data["hint"],
                "solution": data["solution"]
            }
            enigmas.append(enigma)
        return enigmas
