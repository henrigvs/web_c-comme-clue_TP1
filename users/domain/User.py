import uuid


class User:

    def __init__(self, name, lastName, password, email, isConnected=False):
        self.userId = str(uuid.uuid4())
        self.name = name
        self.lastName = lastName
        self.password = password
        self.email = email
        self.isConnected = isConnected

    def __repr__(self) -> str:
        return self.userId + " - " + self.name + " - " + self.lastName + " - " + self.password + " - " + self.email

