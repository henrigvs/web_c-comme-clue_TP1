import requests
from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash

from src.application.form.UserForm import SignInForm

signUpBP = Blueprint('signUp', __name__)
PORT = 5000


@signUpBP.route('/', methods=['GET', 'POST'])
def signUpUser():
    form = SignInForm()

    if form.validate_on_submit():
        firstName = form.firstName.data
        lastName = form.lastName.data
        email = form.email.data
        password = generate_password_hash(form.password.data, "sha256")

        payload = {
            "firstName": firstName,
            "lastName": lastName,
            "email": email,
            "password": password,
            "role": "player"
        }

        # Call user API with JSON payload to add user in DB
        response = requests.post(f"http://localhost:{PORT}/users/addUser", json=payload)
        data = response.json()
        if response.status_code == 201:
            return render_template('user/register_confirmation.html',
                                   userFirstName=firstName)
        else:
            return render_template('user/signUp.html', form=form, error=data['message'])
    else:
        return render_template('user/signUp.html', form=form)
