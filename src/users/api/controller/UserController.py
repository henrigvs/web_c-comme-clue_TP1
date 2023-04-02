from flask import Blueprint, jsonify, request

from src.users.api.service.UserService import UserService
from src.users.api.service.dtos.CreateUserDTO import CreateUserDTO
from src.users.api.service.dtos.UserDTO import UserDTO


class UserController:
    userBP = Blueprint('users', __name__)

    def __init__(self, userService: UserService):
        self.userService = userService

    @userBP.route('/addUser', methods=['POST'])
    def addUser(self):
        data = request.get_json()
        createUserDTO = CreateUserDTO(data['firstName'],
                                      data['lastName'],
                                      data['password'],
                                      data['email'],
                                      False)
        self.userService.addUser(createUserDTO)
        return jsonify(self.userService.addUser(createUserDTO), "user successfully created", "user not created"), 201

    @userBP.route('/allUsers', methods=['GET'])
    def getAllUsers(self):
        userDTOs = self.userService.getAllUsers()
        temp = [userDTO.toJSON for userDTO in userDTOs]
        return jsonify(temp), 200

    @userBP.route('/<userId>', methods=['GET'])
    def getUserById(self, userId):
        userDTO = self.userService.getUserByUserId(userId)
        return self.jsonifyUserDTO(userDTO, "GET request completed", "userId unknown")

    @userBP.route('/<user_id>', methods=['PUT'])
    def editUser(self, user_id):
        data = request.get_json()
        updatingUserDTO = UserDTO(user_id,
                                  data['firstName'],
                                  data['lastName'],
                                  data['password'],
                                  data['email'],
                                  data['isConnected'])
        userDTO = self.userService.editUser(updatingUserDTO)
        return self.jsonifyUserDTO(userDTO,
                                   "update fully completed",
                                   "Error: user_id unknown")

    @userBP.route('/login', methods=['POST'])
    def connectAnUserByEmailAndPassword(self):
        data = request.get_json()
        email = data['email']
        password = data['password']

        # get the userDTO from userId
        userDTO = self.userService.getUserByEmailAndByPassword(email, password)
        userId = userDTO.userId

        # set isConnected at True
        userDTO.connect()
        updatingUserDTO = UserDTO(userId,
                                  userDTO.firstName,
                                  userDTO.lastName,
                                  userDTO.password,
                                  userDTO.email,
                                  userDTO.isConnected)
        return self.jsonifyUserDTO(self.userService.editUser(updatingUserDTO),
                                   "login successful",
                                   "Invalid email or password")

    @userBP.route('/logout', methods=['PUT'])
    def disconnectAnUserByUserId(self):
        dataUserId = request.get_json()
        userId = dataUserId['userId']
        userDTO = self.userService.getUserByUserId(userId)

        # Set isConnected at False
        userDTO.disconnect()
        updatingUserDTO = UserDTO(userId,
                                  userDTO.firstName,
                                  userDTO.lastName,
                                  userDTO.password,
                                  userDTO.email,
                                  userDTO.isConnected)
        return self.jsonifyUserDTO(self.userService.editUser(updatingUserDTO),
                                   "login successful",
                                   "Invalid email or password")

    @staticmethod
    def jsonifyUserDTO(userDTO: UserDTO, messageOk: str, messageNok: str):
        if userDTO is not None:
            return jsonify({
                'userId': userDTO.userId,
                'firstName': userDTO.firstName,
                'lastName': userDTO.lastName,
                'password': userDTO.password,
                'email': userDTO.email,
                'isConnected': userDTO.isConnected,
                'requestResult': {
                    'success': True,
                    'message': messageOk
                }
            }), 200
        else:
            return jsonify({
                'success': False,
                'message': messageNok
            }), 401
