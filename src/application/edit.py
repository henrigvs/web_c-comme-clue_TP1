import requests

from flask import Blueprint, request, render_template, redirect, url_for

editBP = Blueprint('edit', __name__)

apiUrl = 'http://localhost:5000/enigmas'


@editBP.route('/<id>', methods=['GET'])
def editEnigma(id):
    enigmaData = requests.get(f'{apiUrl}/{id}')
    if enigmaData.status_code != 200:
        return "Error: Unable to fetch data", 500
    enigma = enigmaData.json()
    return render_template('riddles/edit.html'
                           , enigma=enigma)


@editBP.route('/<id>', methods=['POST'])
def updateEnigma(id):
    description = request.form['description']
    solution = request.form['solution']
    hint = request.form['hint']
    difficulty = request.form['difficulty']

    json = {
        'description': description,
        'solution': solution,
        'hint': hint,
        'difficulty': int(difficulty)
    }

    try:
        response = requests.put(f'{apiUrl}/{id}', json=json)
        if response.status_code == 201:
            return redirect(url_for('list.list'))
        else:
            errorMessage = 'Error updating enigma.'
    except Exception as e:
        errorMessage = 'Error updating enigma.'
        print(e)
    return render_template('riddles/edit.html', error_message=errorMessage, enigma=json)


@editBP.route('/<id>', methods=['DELETE'])
def deleteEnigma(id):
    try:
        response = requests.delete(f'{apiUrl}/{id}')
        if response.status_code == 200:
            return redirect(url_for('list.list'))
        else:
            error_message = 'Error deleting enigma.'
    except Exception as e:
        error_message = 'Error deleting enigma.'
        print(e)
