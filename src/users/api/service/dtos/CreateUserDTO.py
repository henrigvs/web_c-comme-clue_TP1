class CreateUserDTO:

    def __init__(self, firstName: str, lastName: str, password: str, email: str, isConnected: bool):
        self.firstName = firstName
        self.lastName = lastName
        self.password = password
        self.email = email
        self.isConnected = isConnected

    def __eq__(self, other):
        if not isinstance(other, CreateUserDTO):
            return False
        return (self.firstName == other.firstName
                and self.lastName == other.lastName
                and self.password == other.password
                and self.email == other.email
                and self.isConnected == other.isConnected)