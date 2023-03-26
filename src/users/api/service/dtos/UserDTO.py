class UserDTO:

    def __init__(self, userId: str, firstName: str, lastName: str, password: str, email: str, isConnected: bool):
        self.userId = userId
        self.firstName = firstName
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
                'firstName': self.firstName,
                'lastName': self.lastName,
                'email': self.email,
                'password': self.password,
                'isConnected': self.isConnected
            }

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, UserDTO):
            return False
        else:
            return (
                    self.userId == o.userId
                    and self.firstName == o.firstName
                    and self.lastName == o.lastName
                    and self.email == o.email
                    and self.password == o.password
                    and self.isConnected == o.isConnected)

