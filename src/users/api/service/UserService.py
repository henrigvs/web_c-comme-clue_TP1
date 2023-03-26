from src.users.api.service.dtos.CreateUserDTO import CreateUserDTO
from src.users.api.service.dtos.UserDTO import UserDTO
from src.users.api.service.mapper.UserMapper import UserMapper
from src.users.domain.User import User


class UserService:

    def __init__(self, userRepository):
        self.userRepository = userRepository

    # POST
    def addUser(self, createUserDTO: CreateUserDTO):
        self.userRepository.addUser(UserMapper.toEntity(createUserDTO))

    # PUT
    def editUser(self, createUserDTO, userId) -> User:
        return self.userRepository.editUser(UserMapper.toEntity(createUserDTO))

    # GET
    def getAllUsers(self):
        return [UserMapper.toDTO(user) for user in self.userRepository.getAllUsers()]

    def getUserByUserId(self, userId):
        return UserMapper.toDTO(self.userRepository.getUserByUserId(userId))

    def getUserByEmailAndByPassword(self, email, password) -> UserDTO:
        return UserMapper.toDTO(self.userRepository.getUserByEmailAndByPassword(email, password))