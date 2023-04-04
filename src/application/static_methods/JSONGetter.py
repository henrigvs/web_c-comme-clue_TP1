import requests

from src.application.static_methods.JSONToERiddles import convertJSONToERiddlesArray


class JSONGetter:

    @staticmethod
    def getRiddlesJSON():
        riddlesResponse = requests.get("http://localhost:5000/enigmas/")
        enigmas = convertJSONToERiddlesArray(riddlesResponse.json())
        return enigmas
