from flask import Blueprint, request, session, render_template, redirect, url_for, session
import requests
from game.JSONConverter import JSONConverter

gameBP = Blueprint('game', __name__)
pointer = 1

def getEnigmasJSON():
    enigmas_response = requests.get("http://localhost:5000/enigmas/")
    enigmas = JSONConverter.getEnigmasFromJSON(enigmas_response.json())
    session['enigmas'] = enigmas
    return enigmas

def getNextEnigma(notCorrect):
    return render_template('enigmas/game.html'
                           , notCorrect=notCorrect
                           , current_enigma=pointer
                           , enigma=session['current_enigma']['description']
                           , hint=session['current_enigma']['hint']
                           , solution=session['current_enigma']['solution'])


@gameBP.route('/', methods=['GET', 'POST'])
def game():
    global pointer
    enigmas = getEnigmasJSON()
    if request.method == 'POST':
        answer = request.form.get('answer').strip().lower()
        enigma = session['currentEnigma']

        if answer == enigma['solution'].lower():
            pointer += 1

            if pointer-1 >= len(enigmas):
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
