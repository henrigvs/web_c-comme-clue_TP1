import requests

import app
from src.application.static_methods.JSONToERiddles import convertJSONToERiddlesArray


class JSONGetter:

    @staticmethod
    def getRiddlesJSON():
        riddlesResponse = requests.get(f"http://localhost:{app.PORT}/riddles/getAllRiddles")
        riddles = convertJSONToERiddlesArray(riddlesResponse.json())
        return riddles
