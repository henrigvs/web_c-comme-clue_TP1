from flask import Blueprint, jsonify, request

from src.users.api.service.UserService import UserService
from src.users.api.service.dtos.CreateUserDTO import CreateUserDTO
from src.users.api.service.dtos.UserDTO import UserDTO
from src.users.domain.User import User
from src.users.domain.UserRepository import UserRepository

# Blueprint
userBP = Blueprint('users', __name__)

# Instantiation of the users management system
userRepository = UserRepository()
userService = UserService(userRepository)

# Creation of a data (to remove later by DB implementation)
userRepository.addUser(User("Henri", "Gevenois", "1234", "henri.gevenois@student.unamur.be", False))


@userBP.route('/addUser', methods=['POST'])
def addUser():
    data = request.get_json()
    createUserDTO = CreateUserDTO(data['firstName'],
                                  data['lastName'],
                                  data['password'],
                                  data['email'],
                                  False)
    return jsonifyUserDTO(userService.addUser(createUserDTO),
                          201,
                          "email already exists",
                          400
                          )


@userBP.route('/allUsers', methods=['GET'])
def getAllUsers():
    userDTOs = userService.getAllUsers()
    users = []
    for userDTO in userDTOs:
        user = {
            'userId': userDTO.userId,
            'firstName': userDTO.firstName,
            'lastName': userDTO.lastName,
            'email': userDTO.email,
            'isConnected': userDTO.isConnected
        }
        users.append(user)
    return jsonify(users), 200


@userBP.route('/<userId>', methods=['GET'])
def getUserById(userId):
    userDTO = userService.getUserByUserId(userId)
    return jsonifyUserDTO(userDTO, 200, "userId unknown", 404)


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
    return jsonifyUserDTO(userDTO,
                          200,
                          "userId unknown",
                          404)


@userBP.route('/login', methods=['PUT'])
def connectAnUserByEmailAndPassword():
    data = request.get_json()
    email = data['email']
    password = data['password']

    # get the userDTO from userId
    userDTO = userService.getUserByEmailAndByPassword(email, password)
    userId = userDTO.userId

    # set isConnected at True
    userDTO.connect()
    updatingUserDTO = UserDTO(userId,
                              userDTO.firstName,
                              userDTO.lastName,
                              userDTO.password,
                              userDTO.email,
                              userDTO.isConnected)
    return jsonifyUserDTO(userService.editUser(updatingUserDTO),
                          200,
                          "Wrong email or password",
                          400)


@userBP.route('/logout', methods=['PUT'])
def disconnectAnUserByUserId():
    dataUserId = request.get_json()
    userId = dataUserId['userId']
    userDTO = userService.getUserByUserId(userId)

    # Set isConnected at False
    userDTO.disconnect()
    updatingUserDTO = UserDTO(userId,
                              userDTO.firstName,
                              userDTO.lastName,
                              userDTO.password,
                              userDTO.email,
                              userDTO.isConnected)
    return jsonifyUserDTO(userService.editUser(updatingUserDTO),
                          200,
                          "userId unknown",
                          404)


def jsonifyUserDTO(userDTO: UserDTO, codeOk: int, messageNok: str, codeKo: int):
    if userDTO is not None:
        return jsonify({
            'userId': userDTO.userId,
            'firstName': userDTO.firstName,
            'lastName': userDTO.lastName,
            'password': userDTO.password,
            'email': userDTO.email,
            'isConnected': userDTO.isConnected,
        }), codeOk
    else:
        return jsonify({
            'success': False,
            'message': messageNok
        }), codeKo
