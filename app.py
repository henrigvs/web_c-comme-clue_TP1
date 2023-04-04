from flask import Flask, render_template

from src.application.LoginUser import loginBP
from src.application.edit import editBP
from src.application.game import gameBP
from src.application.list import listBP
from src.Riddles.api.controller.RiddleController import riddleBP
from src.users.api.controller.UserController import userBP

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

# If change port here, should modify into blueprints
PORT = 5000
BASE_URL = f"http://localhost:{PORT}"
app.secret_key = "secretKey"

app.register_blueprint(gameBP, url_prefix='/game')
app.register_blueprint(riddleBP, url_prefix='/riddles')
app.register_blueprint(listBP, url_prefix='/list')
app.register_blueprint(editBP, url_prefix='/edit')
app.register_blueprint(loginBP, url_prefix='/login')
app.register_blueprint(userBP, url_prefix='/users')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('error/404.html'), 404


@app.route('/')
def getIndex():
    return render_template('riddles/index.html')


if __name__ == '__main__':
    app.run(debug=True, port=PORT)
