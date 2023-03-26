from typing import Dict, List, Optional

from src.users.domain.User import User


class UserRepository:

    def __init__(self) -> None:
        self.usersRepository: Dict[str, User] = {}

    def addUser(self, user: User) -> None:
        email = user.email
        for existingUser in self.usersRepository.values():
            if existingUser.email == email:
                raise Exception(f"Email {email} already exists in repository")
        self.usersRepository[user.userId] = user

    def editUser(self, user: User, userId: str) -> User:
        if userId in self.usersRepository:
            self._updateUserProperties(userId, user)
            return self.usersRepository[userId]
        else:
            return None

    def getAllUsers(self) -> List[User]:
        return list(self.usersRepository.values())

    def getUserByUserId(self, userId) -> Optional[User]:
        return self.usersRepository.get(userId)

    def getUserByEmailAndByPassword(self, email: str, password: str) -> Optional[User]:
        for user in self.usersRepository.values():
            if user.email == email and user.password == password:
                return user
        return None

    def _updateUserProperties(self, userId: str, user: User) -> None:

        email = user.email
        for existingUser in self.usersRepository.values():
            if existingUser.email == email and existingUser.userId != userId:
                raise Exception(f"Email {email} already exists in repository")

        self.usersRepository[userId].firstName = user.firstName
        self.usersRepository[userId].lastName = user.lastName
        self.usersRepository[userId].password = user.password
        self.usersRepository[userId].email = user.email
        self.usersRepository[userId].isConnected = user.isConnected
