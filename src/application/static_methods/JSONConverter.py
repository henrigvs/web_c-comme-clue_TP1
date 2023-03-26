class JSONConverter:

    @staticmethod
    def convertJSONToEnigmaArray(jsonData) -> []:
        enigmas = []
        for data in jsonData:
            enigma = {
                "id": data["id"],
                "description": data["description"],
                "hint": data["hint"],
                "solution": data["solution"],
                "difficulty": data["difficulty"]
            }
            enigmas.append(enigma)
        return enigmas
