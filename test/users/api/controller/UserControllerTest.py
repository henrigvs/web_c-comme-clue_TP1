import unittest
from flask import json, current_app

from src.users.api.controller.UserController import UserController
from src.users.api.service.UserService import UserService
from src.users.api.service.dtos.CreateUserDTO import CreateUserDTO
from src.users.domain.UserRepository import UserRepository
from flask import Flask


class UserControllerTest(unittest.TestCase):

    def setUp(self):
        # Initialization of objects for tests
        self.userRepository = UserRepository()
        self.userService = UserService(self.userRepository)
        self.userController = UserController(self.userService)

        # Setting up Flask test client
        self.test_app = Flask(__name__)
        self.test_app.config['TESTING'] = True
        self.test_app.config['DEBUG'] = True  # Enable debug mode
        self.test_app.register_blueprint(self.userController.userBP, url_prefix='/users')
        self.client = self.test_app.test_client()

    def test_addUser(self):
        data = {
            'firstName': 'Ada',
            'lastName': 'Lovelace',
            'email': 'ada.lovelace@example.com',
            'password': 'password123'
        }
        response = self.client.post("/users/addUser", json=data)
        print(response.data)  # Print the response data
        self.assertEqual(201, response.status_code)

        json_data = json.loads(response.data)
        self.assertIsNotNone(json_data['userId'])
        self.assertEqual(json_data['firstName'], data['firstName'])
        self.assertEqual(json_data['lastName'], data['lastName'])
        self.assertEqual(json_data['email'], data['email'])

    def test_getAllUsers(self):
        # Add users before making the request
        self._add_test_users()

        response = self.client.get('/allUsers')
        self.assertEqual(200, response.status_code)

        json_data = json.loads(response.data)
        self.assertEqual(len(json_data), 2)

    def test_getUserById(self):
        # Add user before making the request
        user = self._add_test_user()

        response = self.client.get(f'/{user.userId}')
        self.assertEqual(response.status_code, 200)

        json_data = json.loads(response.data)
        self.assertEqual(json_data['userId'], user.userId)

    # Add other test cases for remaining routes

    def _add_test_users(self):
        users = [
            {
                'firstName': 'Ada',
                'lastName': 'Lovelace',
                'email': 'ada.lovelace@example.com',
                'password': 'password123',
                'isConnected': False,
            },
            {
                'firstName': 'Alan',
                'lastName': 'Turing',
                'email': 'alan.turing@example.com',
                'password': 'password456',
                'isConnected': False,
            },
        ]
        for user in users:
            self.userService.addUser(CreateUserDTO(**user))

    def _add_test_user(self):
        data = {
            'firstName': 'Ada',
            'lastName': 'Lovelace',
            'email': 'ada.lovelace@example.com',
            'password': 'password123',
            'isConnected': False,
        }
        return self.userService.addUser(CreateUserDTO(**data))

