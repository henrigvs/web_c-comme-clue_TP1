from uuid import UUID

import pytest
from unittest.mock import Mock
from src.users.api.controller.UserController import UserController
from src.users.api.service.UserService import UserService
from src.users.api.service.dtos.CreateUserDTO import CreateUserDTO
from src.users.api.service.dtos.UserDTO import UserDTO

# Test data
userId = "d7c09d5c-889d-4e1b-930e-d59117800d93"
userDTO = UserDTO(userId, "Ada", "Lovelace", "ada.lovelace@example.com", "password123", True)
createUserDTO = CreateUserDTO(userDTO.firstName, userDTO.lastName, userDTO.password, userDTO.email, userDTO.isConnected)


def test_editUser():
    # Mocking
    userServiceMock = Mock(spec=UserService)
    userController = UserController(userServiceMock)
    userServiceMock.editUser.return_value = userDTO

    # Execution
    editedUser = userController.editUser(userDTO.userId, userDTO.firstName, userDTO.lastName, userDTO.password,
                                         userDTO.email, userDTO.isConnected)

    # Verification
    userServiceMock.editUser.assert_called_with(createUserDTO, userDTO.userId)
    assert editedUser == userDTO


def test_addUser():
    # Mocking
    userServiceMock = Mock(spec=UserService)
    userController = UserController(userServiceMock)
    userServiceMock.addUser.return_value = userDTO

    # Execution
    newUser = userController.addUser(userDTO.firstName, userDTO.lastName, userDTO.password, userDTO.email,
                                     userDTO.isConnected)

    # Verification
    userServiceMock.addUser.assert_called_with(createUserDTO)
    assert newUser == userDTO


def test_getAllUsers():
    # Mocking
    userServiceMock = Mock(spec=UserService)
    userController = UserController(userServiceMock)
    userServiceMock.getAllUsers.return_value = [userDTO]

    # Execution
    allUsers = userController.getAllUsers()

    # Verification
    userServiceMock.getAllUsers.assert_called()
    assert allUsers == [userDTO]


def test_getUserById():
    # Mocking
    userServiceMock = Mock(spec=UserService)
    userController = UserController(userServiceMock)
    userServiceMock.getUserByUserId.return_value = userDTO

    # Execution
    user = userController.getUserById(userDTO.userId)

    # Verification
    userServiceMock.getUserByUserId.assert_called_with(userDTO.userId)
    assert user == userDTO


def test_getUserByEmailAndByPassword():
    # Mocking
    userServiceMock = Mock(spec=UserService)
    userController = UserController(userServiceMock)
    userServiceMock.getUserByEmailAndByPassword.return_value = userDTO

    # Execution
    user = userController.getUserByEmailAndByPassword(userDTO.email, userDTO.password)

    # Verification
    userServiceMock.getUserByEmailAndByPassword.assert_called_with(userDTO.email, userDTO.password)
    assert user == userDTO
