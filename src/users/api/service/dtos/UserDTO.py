from typing import Dict

from src.users.domain.Role import Role


class UserDTO:

    def __init__(self, userId: str, firstName: str, lastName: str, password: str, email: str, role: Role,
                 isConnected: bool):
        self.userId = userId
        self.firstName = firstName
        self.lastName = lastName
        self.password = password
        self.email = email
        self.role = role
        self.isConnected = isConnected

    def connect(self) -> None:
        self.isConnected = True

    def disconnect(self):
        self.isConnected = False

    def to_dict(self) -> dict:
        return {
            'userId': self.userId,
            'firstName': self.firstName,
            'lastName': self.lastName,
            'password': self.password,
            'email': self.email,
            'role': self.role.label,
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
                    and self.role == o.role
                    and self.isConnected == o.isConnected)

    def __repr__(self):
        return f"UserDTO(userId={self.userId!r}, " \
               f"firstName={self.firstName!r}, " \
               f"lastName={self.lastName!r}, " \
               f"password={self.password!r}, " \
               f"email={self.email!r}, " \
               f"role={self.role.label!r}"\
               f"isConnected={self.isConnected})"
