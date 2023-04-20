import binascii
import os

from flask import Flask, render_template

from database.database import init_db
from src.application.users_login.LoginUser import loginBP
from src.application.edit import editBP
from src.application.game import gameBP
from src.application.List import listBP
from src.riddles.api.controller.RiddleController import riddleBP
from src.users.api.controller.UserController import userBP
from src.application.users_login.SignUpUser import signUpBP

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
basedir = os.path.abspath(os.path.dirname(__file__))

# Configure and init DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database', 'vicious_clue_database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
init_db(app)

# If change port here, should modify into blueprints
PORT = 5000
app.secret_key = binascii.hexlify(os.urandom(24))

app.register_blueprint(gameBP, url_prefix='/game')
app.register_blueprint(riddleBP, url_prefix='/riddles')
app.register_blueprint(listBP, url_prefix='/list')
app.register_blueprint(editBP, url_prefix='/edit')
app.register_blueprint(loginBP, url_prefix='/login')
app.register_blueprint(userBP, url_prefix='/users')
app.register_blueprint(signUpBP, url_prefix='/signUp')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('error/404.html'), 404


@app.route('/')
def getIndex():
    return render_template('riddles/index.html')


if __name__ == '__main__':
    app.run(debug=True, port=PORT)
