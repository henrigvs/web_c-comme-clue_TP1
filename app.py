from flask import Flask, render_template

from src.Enigmas.api.MyEnigmaAPI import enigmaBP
from src.application.game import gameBP
from src.application.edit import editBP
from src.application.LoginUser import loginBP
from src.users.api.MyUserAPI import MyUserAPI
from src.application.list import listBP
from src.users.api.controller.UserController import UserController
from src.users.api.service.UserService import UserService
from src.users.domain.UserRepository import UserRepository

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
PORT = 5000
BASE_URL = f"http://localhost:{PORT}"
app.secret_key = "secretKey"

app.register_blueprint(gameBP, url_prefix='/game')
app.register_blueprint(enigmaBP, url_prefix='/enigmas')
app.register_blueprint(listBP, url_prefix='/list')
app.register_blueprint(editBP, url_prefix='/edit')
app.register_blueprint(loginBP, url_prefix='/login')

# Instantiation of the users management system
userRepository = UserRepository()
userService = UserService(userRepository)
userController = UserController(userService)
myUserAPI = MyUserAPI(userController)


# Creation of a data (to remove later by DB implementation)
userController.addUser("Henri", "Gevenois", "1234", "henri.gevenois@student.unamur.be", False)


# Register the blueprints
app.register_blueprint(myUserAPI.userBP, url_prefix='/users')


@app.route('/')
def getIndex():
    return render_template('enigmas/index.html')


if __name__ == '__main__':
    app.run(debug=True, port=PORT)
