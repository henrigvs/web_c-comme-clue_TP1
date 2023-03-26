from uuid import UUID
from unittest.mock import Mock, patch
from src.users.api.service.UserService import UserService
from src.users.api.service.dtos.CreateUserDTO import CreateUserDTO
from src.users.api.service.mapper.UserMapper import UserMapper
from src.users.domain.User import User

# Initialisation des objets pour les tests
userMapper = UserMapper()
user = User("Ada", "Lovelace", "ada.lovelace@example.com", "password123")
userId = "d7c09d5c-889d-4e1b-930e-d59117800d93"
user.userId = userId
userDTO = userMapper.toDTO(user)
createUserDTO = CreateUserDTO(userDTO.firstName, userDTO.lastName, userDTO.password, userDTO.email, userDTO.isConnected)


@patch('uuid.uuid4', return_value=UUID(userId))
def test_addUser(mock_uuid4):
    userRepositoryMock = Mock()
    userService = UserService(userRepositoryMock)

    userService.addUser(createUserDTO)

    userRepositoryMock.addUser.assert_called_once()
    assert userRepositoryMock.addUser.call_args[0][0] == userMapper.toEntity(
        createUserDTO), f"Expected call not found. Expected: {userMapper.toEntity(createUserDTO)}, Actual: {userRepositoryMock.addUser.call_args[0][0]}"


@patch('uuid.uuid4', return_value=UUID(userId))
def test_editUser(mock_uuid4):
    userRepositoryMock = Mock()
    userService = UserService(userRepositoryMock)
    userRepositoryMock.editUser.return_value = user

    editedUser = userService.editUser(userDTO, 1)

    userRepositoryMock.editUser.assert_called_with(userMapper.toEntity(userDTO), 1)
    assert editedUser == user


def test_getAllUsers():
    userRepositoryMock = Mock()
    userService = UserService(userRepositoryMock)
    userRepositoryMock.getAllUsers.return_value = [user]

    allUsers = userService.getAllUsers()

    userRepositoryMock.getAllUsers.assert_called()
    assert allUsers[0].firstName == userDTO.firstName
    assert allUsers[0].lastName == userDTO.lastName


def test_getUserByUserId():
    userRepositoryMock = Mock()
    userService = UserService(userRepositoryMock)
    userRepositoryMock.getUserByUserId.return_value = user

    userResult = userService.getUserByUserId(user.userId)

    userRepositoryMock.getUserByUserId.assert_called_with(user.userId)
    assert userResult == UserMapper.toDTO(user)


def test_getUserByEmailAndByPassword():
    user_repository_mock = Mock()
    user_service = UserService(user_repository_mock)
    user_repository_mock.getUserByEmailAndByPassword.return_value = user

    user_result = user_service.getUserByEmailAndByPassword("ada.lovelace@example.com", "password123")

    user_repository_mock.getUserByEmailAndByPassword.assert_called_with("ada.lovelace@example.com", "password123")
    assert user_result == UserMapper.toDTO(user)
