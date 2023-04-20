import uuid

from src.users.domain import Role


class User:

    def __init__(self, firstName: str, lastName: str, password: str, email: str, role: Role, isConnected=False, userId: str = None):
        self.userId = userId if userId else str(uuid.uuid4())
        self.firstName = firstName
        self.lastName = lastName
        self.password = password
        self.email = email
        self.role = role
        self.isConnected = isConnected

    def __repr__(self) -> str:
        return self.userId + " - " + self.firstName + " - " + self.lastName + " - " + self.password + " - " + self.email + " - " + self.role.label + " - " + self.isConnected.__repr__()

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, User):
            return False
        return (
            self.firstName == o.firstName
            and self.lastName == o.lastName
            and self.email == o.email
            and self.password == o.password
            and self.role == o.role
        )


