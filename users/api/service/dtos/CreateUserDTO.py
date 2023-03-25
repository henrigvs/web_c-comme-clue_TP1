class CreateUserDTO:

    def __init__(self, name, lastName, password, email, isConnected):
        self.name = name
        self.lastName = lastName
        self.password = password
        self.email = email
        self.isConnected = isConnected
