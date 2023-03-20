from flask import Blueprint, request, session, render_template, redirect, url_for, session
import requests

from game.JSONConverter import JSONConverter

gameBP = Blueprint('game', __name__)
currentEnigma = 1

def getEnigmasJSON():
    enigmas_response = requests.get("http://localhost:5000/enigmas/")
    enigmas = JSONConverter.getEnigmasFromJSON(enigmas_response.json())
    session['enigmas'] = enigmas
    return enigmas

def goToNextEnigma():
    return render_template('enigmas/game.html'
                           , not_correct=False
                           , current_enigma=currentEnigma
                           , enigma=session['current_enigma']['description']
                           , hint=session['current_enigma']['hint']
                           , solution=session['current_enigma']['solution'])

def goToSameEnigma():
    return render_template('enigmas/game.html'
                           , not_correct=True
                           , current_enigma=currentEnigma
                           , enigma=session['current_enigma']['description']
                           , hint=session['current_enigma']['hint']
                           , solution=session['current_enigma']['solution'])

@gameBP.route('/', methods=['GET', 'POST'])
def game():
    global currentEnigma
    if request.method == 'POST':
        answer = request.form.get('answer').strip().lower()
        enigma = session['current_enigma']

        if answer == enigma['solution'].lower():
            currentEnigma += 1
            enigmas = getEnigmasJSON()
            if currentEnigma-1 >= len(enigmas):
                currentEnigma = 1
                return render_template("enigmas/game_completed.html")

            else:
                enigmas = getEnigmasJSON()
                session['current_enigma'] = enigmas[currentEnigma - 1]
                return goToNextEnigma()

        else:
            return goToSameEnigma()

    else:
        enigmas = getEnigmasJSON()
        session['current_enigma'] = enigmas[currentEnigma-1]
        return goToNextEnigma()
