from flask import Blueprint, jsonify, request

from src.users.api.service.UserService import UserService
from src.users.api.service.dtos.CreateUserDTO import CreateUserDTO
from src.users.api.service.dtos.UserDTO import UserDTO
from src.users.domain.User import User
from src.users.domain.UserRepository import UserRepository

userBP = Blueprint('users', __name__)

userRepository = UserRepository()
userService = UserService(userRepository)

userRepository.addUser(User("Henri", "Gevenois", "1234", "henri.gevenois@student.unamur.be", False))


@userBP.route('/addUser', methods=['POST'])
def addUser():
    data = request.get_json()
    createUserDTO = CreateUserDTO(data['firstName'],
                                  data['lastName'],
                                  data['password'],
                                  data['email'],
                                  False)
    userDTO = userService.addUser(createUserDTO)
    return jsonify_userDTO(userDTO, 201, "email already exists", 400)


@userBP.route('/allUsers', methods=['GET'])
def getAllUsers():
    userDTOs = userService.getAllUsers()
    users = [userDTO.to_dict() for userDTO in userDTOs]
    return jsonify(users), 200


@userBP.route('/<userId>', methods=['GET'])
def getUserById(userId):
    userDTO = userService.getUserByUserId(userId)
    return jsonify_userDTO(userDTO, 200, "userId unknown", 404)


@userBP.route('/delete/<userId>', methods=['DELETE'])
def deleteUserByUserId(userId):
    userDTO = userService.deleteUserByUserId(userId)
    return jsonify_userDTO(userDTO, 200, "userId unknown", 404)


@userBP.route('/<user_id>', methods=['PUT'])
def editUser(user_id):
    data = request.get_json()
    updatingUserDTO = UserDTO(user_id,
                              data['firstName'],
                              data['lastName'],
                              data['password'],
                              data['email'],
                              data['isConnected'])
    userDTO = userService.editUser(updatingUserDTO)
    return jsonify_userDTO(userDTO, 200, "userId unknown", 404)


@userBP.route('/login', methods=['PUT'])
def connectAnUserByEmailAndPassword():
    data = request.get_json()
    email, password = data['email'], data['password']
    userDTO = userService.getUserByEmailAndByPassword(email, password)
    userDTO.connect()
    updatedUserDTO = userService.editUser(userDTO)
    return jsonify_userDTO(updatedUserDTO, 200, "Wrong email or password", 400)


@userBP.route('/logout', methods=['PUT'])
def disconnectAnUserByUserId():
    userId = request.get_json()['userId']
    userDTO = userService.getUserByUserId(userId)
    userDTO.disconnect()
    updatedUserDTO = userService.editUser(userDTO)
    return jsonify_userDTO(updatedUserDTO, 200, "userId unknown", 404)


def jsonify_userDTO(userDTO: UserDTO, code_ok: int, message_nok: str, code_ko: int):
    if userDTO is not None:
        return jsonify(userDTO.to_dict()), code_ok
    else:
        return jsonify({'success': False, 'message': message_nok}), code_ko
