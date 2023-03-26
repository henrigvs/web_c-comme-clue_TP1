from flask import request, jsonify, Blueprint

from src.users.api.controller.UserController import UserController
from src.users.api.service.dtos.UserDTO import UserDTO


class MyUserAPI:
    userBP = Blueprint('users', __name__)

    def __init__(self, userController: UserController):
        self.userController = userController

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

    @userBP.route('/', methods=['POST'])
    def addUser(self):
        data = request.get_json()
        self.userController.addUser(data['firstName'], data['lastName'], data['password'], data['email'], False)
        return jsonify({'success': True}), 201

    @userBP.route('/allUsers', methods=['GET'])
    def getAllUsers(self):
        userDTOs = self.userController.getAllUsers()
        temp = [userDTO.toJSON() for userDTO in userDTOs]
        return jsonify(temp), 200

    @userBP.route('/<userId>', methods=['GET'])
    def getUserById(self, userId):
        userDTO = self.userController.getUserById(userId)
        return self.jsonifyUserDTO(userDTO, "GET request completed", "userId unknown")

    @userBP.route('/<user_id>', methods=['PUT'])
    def editUser(self, user_id):
        data = request.get_json()
        userDTO = self.userController.editUser(user_id, data['firstName'], data['lastName'], data['password'],
                                               data['email'],
                                               data['isConnected'])
        return self.jsonifyUserDTO(userDTO, "update fully completed", "Error: user_id unknown")

    @userBP.route('/login', methods=['POST'])
    def connectAnUserByEmailAndPassword(self):
        data = request.get_json()
        email = data['email']
        password = data['password']

        # get the userDTO from userId
        userDTO = self.userController.getUserByEmailAndByPassword(email, password)
        userId = userDTO.userId

        # set isConnected at True
        userDTO.connect()
        self.userController.editUser(userId, userDTO.firstName, userDTO.lastName, userDTO.password, userDTO.email,
                                     userDTO.isConnected)
        return self.jsonifyUserDTO(userDTO, "login successful", "Invalid email or password")

    @userBP.route('/logout', methods=['PUT'])
    def disconnectAnUserByUserId(self):
        dataUserId = request.get_json()
        userId = dataUserId['userId']
        userDTO = self.userController.getUserById(userId)

        # Set isConnected at False
        userDTO.disconnect()
        self.userController.editUser(userId, userDTO.firstName, userDTO.lastName, userDTO.password, userDTO.email,
                                     userDTO.isConnected)
        if userDTO is not None:
            return jsonify({'success': True,
                            'message': 'user correctly disconnected'}), 200
        else:
            return jsonify({'success': False,
                            'message': 'userId unknown'}), 401
