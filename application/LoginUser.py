from flask import request, render_template, Blueprint, session, redirect, url_for
import requests

loginBP = Blueprint('login', __name__)
endPoint_getUserByEmailAndByPassword = 'http://localhost:5000/users/login'


@loginBP.route('/', methods=['GET', 'POST'])
def loginUser():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        json = {
            "email": email,
            "password": password
        }

        response = requests.post(f'{endPoint_getUserByEmailAndByPassword}', json=json)
        if response.status_code == 200:
            data = response.json()
            session['userId'] = data['userId']
            session['userName'] = data['name']
            session['userLastName'] = data['lastName']
            session['userEmail'] = data['email']
            session['userIsConnected'] = True
            return render_template("/login/login.html",
                                   userID=session['userId'],
                                   userName=session['userName'],
                                   userLastName=session['userLastName'],
                                   userEmail=session['userEmail'],
                                   userConnectionStatus=session['userIsConnected'])
        else:
            errorMessage = "Error during login, please contact your system administrator"
            return render_template('login/login.html', errorMessage=errorMessage, userConnectionStatus=False)

    else:
        userId = session.get('userId')
        userName = session.get('userName')
        userLastName = session.get('userLastName')
        userEmail = session.get('userEmail')
        userIsConnected = session.get('userIsConnected')

        if userId is None:
            return render_template('login/login.html', userConnectionStatus=False)
        else:

            return render_template("/login/login.html",
                                   userID=userId,
                                   userName=userName,
                                   userLastName=userLastName,
                                   userEmail=userEmail,
                                   userConnectionStatus=userIsConnected)


@loginBP.route('/logout', methods=['POST'])
def logoutUser():
    userId = session.get('userId')
    session.pop('userId', None)
    session.pop('userName', None)
    session.pop('userLastName', None)
    session.pop('userEmail', None)
    session.pop('userIsConnected', None)
    jsonUserId = {"userId": userId}
    requests.put(f'http://localhost:5000/users/logout', json=jsonUserId)
    return redirect(url_for('login.loginUser'))
