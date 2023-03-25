from flask import request, jsonify, Blueprint

from users.api.controller.UserController import UserController
from users.api.service.UserService import UserService
from users.domain.UserRepository import UserRepository

userBP = Blueprint('users', __name__)
userRepository = UserRepository()
userService = UserService(userRepository)
userController = UserController(userService)

# Initializing login(s)
userController.addUser("Henri", "Gevenois", "1234", "henri.gevenois@student.unamur.be", False)


@userBP.route('/', methods=['POST'])
def addUser():
    data = request.get_json()
    userController.addUser(data['name'], data['lastName'], data['password'], data['email'])
    return jsonify({'success': True}), 201


@userBP.route('/allUsers', methods=['GET'])
def getAllUsers():
    return jsonify(userController.getAllUsers())


@userBP.route('/<userId>', methods=['GET'])
def getUserById(userId):
    return jsonify(userController.getUserById(userId))


@userBP.route('/<userID>', methods=['PUT'])
def editUser(userid):
    data = request.get_json()
    userController.editUser(userid, data['name'], data['lastName'], data['password'], data['email'])
    return jsonify({'success': True}), 200


@userBP.route('/login', methods=['POST'])
def connectAnUserByEmailAndPassword():
    data = request.get_json()
    email = data['email']
    password = data['password']
    userDTO = userController.connectUserByEmailAndPassword(email, password)

    if userDTO is not None:
        return jsonify({
            'success': True,
            'message': 'login successful',
            'userId': userDTO.userId,
            'name': userDTO.name,
            'lastName': userDTO.lastName,
            'email': userDTO.email,
            'connectionStatus': userDTO.isConnected
        }), 200
    else:
        return jsonify({
            'success': False,
            'message': 'Invalid email or password'
        }), 401


@userBP.route('/logout', methods=['PUT'])
def disconnectAnUserByUserId():
    dataUserId = request.get_json()
    userId = dataUserId['userId']
    userDTO = userController.getUserById(userId)
    userDTO.disconnect()
    userController.editUser(userId, userDTO.name, userDTO.lastName, userDTO.password, userDTO.email, userDTO.isConnected)
    if userDTO is not None:
        return jsonify({'success': True,
                        'message': 'user correctly disconnected'}), 200
    else:
        return jsonify({'success': False,
                        'message': 'userId unknown'}), 401
