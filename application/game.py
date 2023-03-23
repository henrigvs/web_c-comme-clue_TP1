from flask import Blueprint, request, render_template, session
import requests
from application.static_methods.JSONConverter import JSONConverter

gameBP = Blueprint('game', __name__)
pointer = 1


def getEnigmasJSON():
    enigmas_response = requests.get("http://localhost:5000/enigmas/")
    enigmas = JSONConverter.convertJSONToEnigmaArray(enigmas_response.json())
    return enigmas


def getNextEnigma(notCorrect):
    return render_template('enigmas/game.html'
                           , notCorrect=notCorrect
                           , current_enigma=pointer
                           , enigma=session['currentEnigma']['description']
                           , hint=session['currentEnigma']['hint']
                           , solution=session['currentEnigma']['solution'])


@gameBP.route('/', methods=['GET', 'POST'])
def game():
    global pointer
    enigmas = getEnigmasJSON()
    if request.method == 'POST':
        answer = request.form.get('answer').strip().lower()
        enigma = session['currentEnigma']

        if answer == enigma['solution'].lower():
            pointer += 1

            if pointer - 1 >= len(enigmas):
                pointer = 1
                return render_template("enigmas/game_completed.html")

            else:
                session['currentEnigma'] = enigmas[pointer - 1]
                return getNextEnigma(notCorrect=False)

        else:
            return getNextEnigma(notCorrect=True)

    else:
        session['currentEnigma'] = enigmas[pointer - 1]
        return getNextEnigma(notCorrect=False)
