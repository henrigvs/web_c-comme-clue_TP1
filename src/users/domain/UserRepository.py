from typing import Dict, List, Optional

from src.users.domain.User import User


class UserRepository:

    def __init__(self) -> None:
        self.userRepository: Dict[str, User] = {}

    def addUser(self, user: User) -> User:
        if any(existing_user.email == user.email for existing_user in self.userRepository.values()):
            return None
        self.userRepository[user.userId] = user
        return user

    def editUser(self, user: User, userId: str) -> User:
        if userId not in self.userRepository:
            return None

        self._updateUserProperties(userId, user)
        return self.userRepository[userId]

    def getAllUsers(self) -> List[User]:
        return list(self.userRepository.values())

    def getUserByUserId(self, userId) -> Optional[User]:
        return self.userRepository.get(userId)

    def getUserByEmailAndByPassword(self, email: str, password: str) -> Optional[User]:
        return next(
            (user for user in self.userRepository.values() if user.email == email and user.password == password), None)

    def deleteUserByUserId(self, userId: str) -> User:
        userToBeDeleted = self.getUserByUserId(userId)
        if userToBeDeleted is not None:
            del self.userRepository[userId]
        return userToBeDeleted

    def _updateUserProperties(self, userId: str, user: User) -> None:
        email = user.email
        if any(existing_user.email == email and existing_user.userId != userId for existing_user in
               self.userRepository.values()):
            raise Exception(f"Email {email} already exists in repository")

        self.userRepository[userId].firstName = user.firstName
        self.userRepository[userId].lastName = user.lastName
        self.userRepository[userId].password = user.password
        self.userRepository[userId].email = user.email
        self.userRepository[userId].isConnected = user.isConnected
