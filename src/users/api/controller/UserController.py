from src.users.api.service.UserService import UserService
from src.users.api.service.dtos.CreateUserDTO import CreateUserDTO
from src.users.api.service.dtos.UserDTO import UserDTO
from src.users.api.service.mapper.UserMapper import UserMapper


class UserController:

    def __init__(self, userService: UserService):
        self.userService = userService
        self.userMapper = UserMapper()

    # PUT
    def editUser(self, userId: str, firstName: str, lastName: str, password: str, email: str,
                 isConnected: bool) -> UserDTO:
        return self.userMapper.toDTO(
            self.userService.editUser(CreateUserDTO(firstName, lastName, password, email, isConnected), userId))

    # POST
    def addUser(self, name: str, lastName: str, password: str, email: str, isConnected: bool) -> UserDTO:
        return self.userMapper.toDTO(
            self.userService.addUser(CreateUserDTO(name, lastName, password, email, isConnected)))

    # GET
    def getAllUsers(self) -> []:
        return self.userService.getAllUsers()

    def getUserById(self, id) -> UserDTO:
        return self.userService.getUserByUserId(id)

    def getUserByEmailAndByPassword(self, email, password) -> UserDTO:
        return self.userService.getUserByEmailAndByPassword(email, password)
