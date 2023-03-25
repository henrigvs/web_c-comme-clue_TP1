from flask import Flask, render_template

from Enigmas.api.MyEnigmaAPI import enigmaBP
from application.game import gameBP
from application.edit import editBP
from application.LoginUser import loginBP
from users.api.MyUserAPI import userBP
from application.list import listBP

app = Flask(__name__)
app.secret_key = "secretKey"
app.register_blueprint(gameBP, url_prefix='/game')
app.register_blueprint(enigmaBP, url_prefix='/enigmas')
app.register_blueprint(userBP, url_prefix='/users')
app.register_blueprint(listBP, url_prefix='/list')
app.register_blueprint(editBP, url_prefix='/edit')
app.register_blueprint(loginBP, url_prefix='/login')
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/')
def getIndex():
    return render_template('enigmas/index.html')


if __name__ == '__main__':
    app.run()
