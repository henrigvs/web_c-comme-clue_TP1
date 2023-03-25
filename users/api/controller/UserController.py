from users.api.service.dtos.CreateUserDTO import CreateUserDTO
from users.api.service.dtos.UserDTO import UserDTO


class UserController:

    # POST
    def __init__(self, userService):
        self.userService = userService

    def addUser(self, name, lastName, password, email, isConnected):
        createUserDTO = CreateUserDTO(name, lastName, password, email, isConnected)
        self.userService.addUser(createUserDTO)

    # GET
    def getAllUsers(self):
        userDTOS = self.userService.getAllUsers()
        return [userDTO.toJSON() for userDTO in userDTOS]

    def getUserById(self, id):
        return self.userService.getUserByUserId(id)


    def getUserByEmailAndByPassword(self, email, password):
        userDTO = self.userService.getUserByEmailAndByPassword(email, password)
        if userDTO:
            return userDTO.toJSON()
        else:
            return None

    def getUserByFullName(self, name, lastName):
        userDTO = self.userService.getUserByFullName(name, lastName)
        return userDTO.toJSON()

    # PUT
    def editUser(self, userId, name, lastName, password, email, isConnected):
        return self.userService.editUser(CreateUserDTO(name, lastName, password, email, isConnected), userId)

    def connectUserByEmailAndPassword(self, email, password):
        return self.userService.connectUserByEmailAndPassword(email, password)

