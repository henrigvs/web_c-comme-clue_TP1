from flask import request, jsonify, Blueprint

from users.api.controller.UserController import UserController
from users.api.controller.UserService import UserService
from users.domain.UserRepository import UserRepository

userBP = Blueprint('user', __name__)
userRepository = UserRepository()
userService = UserService(userRepository)
userController = UserController(userService)

# Initializing user(s)
userController.addUser("Henri", "Gevenois", "1234", "henri.gevenois@student.unamur.be")


@userBP.route('/', methods=['POST'])
def addUser():
    data = request.get_json()
    userController.addUser(data['name'], data['lastName'], data['password'], data['email'])
    return jsonify({'success': True}), 201


@userBP.route('/allUsers', methods=['GET'])
def getAllUsers():
    temp = jsonify(userController.getAllUsers())
    return temp


@userBP.route('/<userId>', methods=['GET'])
def getUserById(userId):
    return jsonify(userController.getUserById(int(userId)))


@userBP.route('/login', methods=['POST'])
def loginUser():
    data = request.get_json()
    email = data['email']
    password = data['password']
    user = userController.getUserByEmailAndByPassword(email, password)

    if user is not None:
        return jsonify({
            'success': True,
            'message': 'login successful',
            'user': user
        }), 200
    else:
        return jsonify({
            'success': False,
            'message': 'Invalid email or password'
        }), 401
