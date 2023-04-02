from typing import List

from src.users.api.service.dtos.CreateUserDTO import CreateUserDTO
from src.users.api.service.dtos.UserDTO import UserDTO
from src.users.api.service.mapper.UserMapper import UserMapper
from src.users.domain.User import User


class UserService:

    def __init__(self, userRepository):
        self.userRepository = userRepository
        self.userMapper = UserMapper()

    # POST
    def addUser(self, createUserDTO: CreateUserDTO) -> UserDTO:
        user = self.userRepository.addUser(UserMapper.toEntity(createUserDTO))
        newUserDTO = self.userMapper.toDTO(user)
        return newUserDTO

    # PUT
    def editUser(self, updatingUserDTO: UserDTO) -> UserDTO:
        user = User(updatingUserDTO.firstName,
                    updatingUserDTO.lastName,
                    updatingUserDTO.password,
                    updatingUserDTO.email,
                    updatingUserDTO.isConnected)
        updatedUser = self.userRepository.editUser(user, updatingUserDTO.userId)
        updatedUserDTO = self.userMapper.toDTO(updatedUser)
        return updatedUserDTO

    # GET
    def getAllUsers(self) -> List[UserDTO]:
        return [UserMapper.toDTO(user) for user in self.userRepository.getAllUsers()]

    def getUserByUserId(self, userId: str) -> UserDTO:
        return UserMapper.toDTO(self.userRepository.getUserByUserId(userId))

    def getUserByEmailAndByPassword(self, email: str, password: str) -> UserDTO:
        return UserMapper.toDTO(self.userRepository.getUserByEmailAndByPassword(email, password))