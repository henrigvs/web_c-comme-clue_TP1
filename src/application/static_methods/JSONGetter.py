import requests

from src.application.static_methods.JSONToERiddles import convertJSONToERiddlesArray


class JSONGetter:

    @staticmethod
    def getRiddlesJSON():
        riddlesResponse = requests.get(f"http://localhost:5000/riddles/getAllRiddles")
        riddles = convertJSONToERiddlesArray(riddlesResponse.json())
        return riddles
