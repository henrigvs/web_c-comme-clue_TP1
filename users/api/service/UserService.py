from users.api.service.mapper.UserMapper import UserMapper


class UserService:

    def __init__(self, userRepository):
        self.userRepository = userRepository

    # POST
    def addUser(self, userDTO):
        self.userRepository.addUser(UserMapper.toEntity(userDTO))

    def editUser(self, createUserDTO, userId):
        self.userRepository.editUser(UserMapper.toEntity(createUserDTO), userId)

    # GET
    def getAllUsers(self):
        return [UserMapper.toDTO(user) for user in self.userRepository.getAllUsers()]

    def getUserByUserId(self, userId):
        return UserMapper.toDTO(self.userRepository.getUserByUserId(userId))

    def getUserByEmailAndByPassword(self, email, password):
        return UserMapper.toDTO(self.userRepository.getUserByEmailAndByPassword(email, password))

    def connectUserByEmailAndPassword(self, email, password):
        return UserMapper.toDTO(self.userRepository.connectUserByEmailAndPassword(email, password))

    def getUserByFullName(self, name, lastName):
        return UserMapper.toDTO(self.userRepository.getUserByFullName(name, lastName))
