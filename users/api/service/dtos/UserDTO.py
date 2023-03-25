class UserDTO:

    def __init__(self, userId, name, lastName, password, email, isConnected):
        self.userId = userId
        self.name = name
        self.lastName = lastName
        self.password = password
        self.email = email
        self.isConnected = isConnected

    def connect(self):
        self.isConnected = True

    def disconnect(self):
        self.isConnected = False

    def toJSON(self):
        return \
            {
                'userId': self.userId,
                'name': self.name,
                'lastName': self.lastName,
                'email': self.email,
                'password': self.password,
                'isConnected': self.isConnected
            }
