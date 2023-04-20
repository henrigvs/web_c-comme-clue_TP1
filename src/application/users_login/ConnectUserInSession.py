from flask import session
import requests


class ConnectUserInSession:

    @staticmethod
    def connectUser(data: dict):
        session['userId'] = data['userId']
        session['userName'] = data['firstName']
        session['userLastName'] = data['lastName']
        session['userEmail'] = data['email']
        session['userRole'] = data['role']
        session['userIsConnected'] = True
