from users.api.dtos.UserDTO import UserDTO


def jsonUser(user):
    return {'name': user.name,
            'lastName': user.lastName,
            'email': user.email,
            'password': user.password}


class UserController:

    # POST
    def __init__(self, userService):
        self.userService = userService

    def addUser(self, name, lastName, password, email):
        userDTO = UserDTO(name, lastName, password, email)
        self.userService.addUser(userDTO)

    # GET
    def getAllUsers(self):
        users = self.userService.getAllUsers()
        return [jsonUser(user) for user in users]

    def getUserById(self, id):
        user = self.userService.getUserByUserId(id)
        if user:
            return jsonUser(user)
        else:
            return None

    def getUserByEmailAndByPassword(self, email, password):
        user = self.userService.getUserByEmailAndByPassword(email, password)
        if user:
            return jsonUser(user)
        else:
            return None

    def getUserByFullName(self, name, lastName):
        user = self.userService.getUserByFullName(name, lastName)
        return jsonUser(user)
