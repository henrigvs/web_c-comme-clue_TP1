import unittest
from unittest import mock

from flask import url_for, Flask

from src.users.api.MyUserAPI import MyUserAPI
from src.users.api.controller.UserController import UserController
from src.users.api.service.UserService import UserService
from src.users.api.service.dtos.UserDTO import UserDTO
from src.users.domain.User import User
from src.users.domain.UserRepository import UserRepository


class TestRoutes(unittest.TestCase):
    firstName = "Ada"
    lastName = "Lovelace"
    password = "myPassword"
    email = "adalovelace@example.com"
    userId = "d7c09d5c-889d-4e1b-930e-d59117800d93"

    @staticmethod
    def urlMapRulesFlushing(app, endPoint: str):
        for rule in list(app.url_map.iter_rules(endPoint)):
            app.url_map._rules.remove(rule)
        app.view_functions.pop(endPoint, None)

    @staticmethod
    def createApp():
        newApp = Flask(__name__)
        newApp.config['TESTING'] = True
        return newApp

    def setUp(self):
        self.app = self.createApp()
        self.app.config['SERVER_NAME'] = "localhost:5000"
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

        # Mock set up
        self.userRepository = mock.Mock(spec=UserRepository)
        self.userService = UserService(self.userRepository)
        self.userController = UserController(self.userService)
        self.myUserAPI = MyUserAPI(self.userController)
        self.app.register_blueprint(self.myUserAPI.userBP, url_prefix='/users')
        mockUser = User(self.firstName, self.lastName, self.password, self.email)
        self.userRepository.getUserByEmailAndByPassword.return_value = mockUser

    def test_addUser_WhenAValidJSONDataFileIsProvided_ThenAResponseCode201IsReturned(self):
        userData = {
            "firstName": self.firstName,
            "lastName": self.lastName,
            "password": self.password,
            "email": self.email,
        }
        response = self.client.post(url_for('users.addUser'), json=userData)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {"success": True})

    def test_editUser_WhenAValidJSONDataFileIsProvided_ThenAResponseCode200IsReturned(self):
        # Create through endpoint
        userData = {
            "firstName": self.firstName,
            "lastName": self.lastName,
            "password": self.password,
            "email": self.email,
        }
        response = self.client.post(url_for('users.addUser'), json=userData)

        # Retrieve userId
        userData = {
            "email": self.email,
            "password": self.password
        }
        response = self.client.post(url_for('users.connectAnUserByEmailAndPassword'), json=userData)
        userId = response.json['userId']

        # Edit user
        editedUserData = {
            "firstName": self.firstName,
            "lastName": self.lastName,
            "password": "myNewPassword",
            "email": self.email,
            "isConnected": True
        }
        self.userRepository.editUser.return_value = UserDTO(userId, self.firstName, self.lastName, "myNewPassword", self.email, True)
        response = self.client.put(url_for('users.editUser', user_id=userId), json=editedUserData)  # Call the endpoint of editUser()
        responseJson = response.json

        self.assertEqual(response.status_code, 200)
        self.assertEqual(responseJson['email'], self.email)
        self.assertEqual(responseJson['firstName'], self.firstName)
        self.assertEqual(responseJson['lastName'], self.lastName)
        self.assertEqual(responseJson['password'], "myNewPassword")
        self.assertEqual(responseJson['isConnected'], True)
        self.assertEqual(responseJson['requestResult'], {'success': True, 'message': 'update fully completed'})

    def test_getAllUsers(self):
        # Set some users to inject in the repository
        user1 = User("Jean", "Dujardin", "password", "loulou@example.com")
        user2 = User("Alexandra", "Lami", "password", "chouchou@example.com", False)

        # Set up a return value for the mock
        self.userController.getAllUsers.return_value = [self.userMapper.toDTO(), self.userMapper.toDTO()]

        response = self.client.get(url_for('users.getAllUsers'))
        self.assertEqual(response.status_code, 200)

        # Check if the method was called once
        self.userController.getAllUsers.assert_called_once()

    def test_getUserById(self):
        # You might need to replace this with an actual user ID in your system.
        test_user_id = "some-user-id"
        response = self.client.get(url_for('users.getUserById'), userId=test_user_id)
        self.assertEqual(response.status_code, 200)

    def test_connectAnUserByEmailAndPassword(self):
        data = {
            "email": "henri.gevenois@student.unamur.be",
            "password": "1234"
        }
        response = self.client.post(url_for('users.connectAnUserByEmailAndPassword'), json=data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json["requestResult"]["success"])

    def test_disconnect_an_user_by_user_id(self):
        # You might need to replace this with an actual user ID in your system.
        test_user_id = "some-user-id"
        data = {
            "userId": test_user_id
        }
        response = self.client.put(url_for('users.disconnectAnUserByUserId'), json=data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json["success"])

    def tearDown(self):
        self.app_context.pop()




if __name__ == "__main__":
    unittest.main()
