import requests
from application.static_methods.JSONConverter import JSONConverter

class JSONGetter:

    @staticmethod
    def getEnigmasJSON():
        enigmas_response = requests.get("http://localhost:5000/enigmas/")
        enigmas = JSONConverter.convertJSONToEnigmaArray(enigmas_response.json())
        return enigmas