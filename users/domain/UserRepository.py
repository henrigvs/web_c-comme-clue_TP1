
class UserRepository:

    def __init__(self):
        self.usersRepository = {}

    def addUser(self, user):
        self.usersRepository[len(self.usersRepository) + 1] = user

    def getAllUsers(self):
        return self.usersRepository.values()

    def getUserByUserId(self, userId):
        if userId in self.usersRepository:
            return self.usersRepository[userId]
        else:
            return None

    def getUserByEmailAndByPassword(self, email, password):
        for user in self.usersRepository.values():
            if user.email == email and user.password == password:
                return user
        return None

    def getUserByFullName(self, name, lastName):
        for user in self.usersRepository.values():
            if user.name == name and user.lastName == lastName:
                return user
        return None
