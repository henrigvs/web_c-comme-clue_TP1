import unittest
from src.users.api.service.dtos.CreateUserDTO import *
from src.users.api.service.dtos.UserDTO import UserDTO
from src.users.api.service.mapper.UserMapper import UserMapper
from src.users.domain.User import User


class TestUserDTO(unittest.TestCase):

    def test_create_UserDTO(self):
        user_dto = UserDTO('randomID', 'Ada', 'Lovelace', 'password', 'adalovelace@example.com', False)
        self.assertEqual(user_dto.userId, 'random-ID')
        self.assertEqual(user_dto.firstName, 'Ada')
        self.assertEqual(user_dto.lastName, 'Lovelace')
        self.assertEqual(user_dto.password, 'password')
        self.assertEqual(user_dto.email, 'adalovelace@example.com')
        self.assertFalse(user_dto.isConnected)

    def test_connectUser(self):
        userDto = UserDTO('randomID', 'John', 'Doe', 'password', 'johndoe@example.com', False)
        userDto.connect()
        self.assertTrue(userDto.isConnected)

    def test_disconnectUser(self):
        userDto = UserDTO('randomID', 'John', 'Doe', 'password', 'johndoe@example.com', True)
        userDto.disconnect()
        self.assertFalse(userDto.isConnected)


class TestCreateUserDTO(unittest.TestCase):

    def test_create_createUserDTO(self):
        createUserDto = CreateUserDTO('Ada', 'Lovelace', 'password', 'adalovelace@example.com', False)
        self.assertEqual(createUserDto.firstName, 'Ada')
        self.assertEqual(createUserDto.lastName, 'Lovelace')
        self.assertEqual(createUserDto.password, 'password')
        self.assertEqual(createUserDto.email, 'adalovelace@example.com')
        self.assertFalse(createUserDto.isConnected)


class TestUserMapper(unittest.TestCase):

    def test_toDTO(self):
        userMapper = UserMapper
        user = User('Ada', 'Lovelace', 'password', 'adalovelace@example.com', False)
        user.userId = 'testIDd'
        userDto = userMapper.toDTO(user)
        self.assertEqual(userDto.userId, 'testIDd')
        self.assertEqual(userDto.firstName, 'Ada')
        self.assertEqual(userDto.lastName, 'Lovelace')
        self.assertEqual(userDto.password, 'password')
        self.assertEqual(userDto.email, 'adalovelace@example.com')
        self.assertFalse(userDto.isConnected)

    def test_toEntity(self):
        userMapper = UserMapper
        createUserDTO = CreateUserDTO('Ada', 'Lovelace', 'password', 'adalovelace@example.com', False)
        user = userMapper.toEntity(createUserDTO)
        self.assertEqual(user.firstName, 'Ada')
        self.assertEqual(user.lastName, 'Lovelace')
        self.assertEqual(user.password, 'password')
        self.assertEqual(user.email, 'adalovelace@example.com')
        self.assertFalse(user.isConnected)


if __name__ == '__main__':
    unittest.main()
