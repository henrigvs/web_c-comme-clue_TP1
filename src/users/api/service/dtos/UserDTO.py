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
