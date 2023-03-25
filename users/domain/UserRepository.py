class UserRepository:

    def __init__(self):
        self.usersRepository = {}

    def addUser(self, user):
        userId = user.userId
        self.usersRepository[userId] = user

    def editUser(self, user, userId):
        if userId in self.usersRepository:
            self.usersRepository[userId].name = user.name
            self.usersRepository[userId].lastName = user.lastName
            self.usersRepository[userId].password = user.password
            self.usersRepository[userId].email = user.email
            self.usersRepository[userId].isConnected = user.isConnected
        else:
            print("userId doesn't exist in repository")

    def connectUserByEmailAndPassword(self, email, password):
        user = self.getUserByEmailAndByPassword(email, password)
        if user is None:
            return None
        else:
            self.usersRepository[user.userId].isConnected = True
            return user

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
