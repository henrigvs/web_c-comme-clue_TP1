from flask import request, render_template, Blueprint, session, redirect, url_for
import requests

from src.application.users.ConnectUserInSession import ConnectUserInSession

loginBP = Blueprint('login', __name__)
PORT = 5000


@loginBP.route('/', methods=['GET', 'POST'])
def loginUser():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        json = {
            "email": email,
            "password": password
        }

        response = requests.put(f"http://localhost:{PORT}/users/login", json=json)
        if response.status_code == 200:
            data = response.json()
            ConnectUserInSession.connectUser(data)
            return render_template('user/login.html',  # Simplify that !!!
                                   userID=session['userId'],
                                   userName=session['userName'],
                                   userLastName=session['userLastName'],
                                   userEmail=session['userEmail'],
                                   userRole=session['userRole'],
                                   userConnectionStatus=session['userIsConnected'])
        else:
            errorMessage = "Error during login, please contact your system administrator"
            return render_template('user/login.html', errorMessage=errorMessage, userConnectionStatus=False)

    else:
        userId = session.get('userId')
        userName = session.get('userName')
        userLastName = session.get('userLastName')
        userEmail = session.get('userEmail')
        userRole = session.get('userRole')
        userIsConnected = session.get('userIsConnected')

        if userId is None:
            return render_template('user/login.html', userConnectionStatus=False)
        else:

            return render_template('user/login.html',
                                   userID=userId,
                                   userName=userName,
                                   userLastName=userLastName,
                                   userEmail=userEmail,
                                   userRole=userRole,
                                   userConnectionStatus=userIsConnected)


@loginBP.route('/logout', methods=['POST'])
def logoutUser():
    userId = session.get('userId')
    session.pop('userId', None)
    session.pop('userName', None)
    session.pop('userLastName', None)
    session.pop('userEmail', None)
    session.pop('userRole', None)
    session.pop('userIsConnected', None)
    jsonUserId = {"userId": userId}
    requests.put(f"http://localhost:{PORT}/users/logout", json=jsonUserId)
    return redirect(url_for('login.loginUser'))
