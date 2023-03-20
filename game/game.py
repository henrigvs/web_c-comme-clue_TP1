from flask import Blueprint, request, session, render_template, redirect, url_for, session
import requests

from game.JSONConverter import JSONConverter

gameBP = Blueprint('game', __name__)
currentEnigma = 1


@gameBP.route('/', methods=['GET', 'POST'])
def game():
    global currentEnigma
    if 'enigmas' not in session:
        enigmas_response = requests.get("http://localhost:5000/enigmas/")
        enigmas = JSONConverter.getEnigmasFromJSON(enigmas_response.json())
        session['enigmas'] = enigmas
    enigmas = session['enigmas']
    if request.method == 'POST':
        answer = request.form.get('answer').strip().lower()
        enigma = session['current_enigma']
        if answer == enigma['solution'].lower():
            currentEnigma += 1
            if currentEnigma >= len(enigmas):
                return render_template("enigmas/game_completed.html")
            session['current_enigma'] = enigmas[currentEnigma-1]
            return redirect(url_for('game.game'))
        else:
            return render_template('enigmas/game.html', enigma=session['current_enigma']
                                   , hint=session['current_enigma']['hint']
                                   , solution=session['current_enigma']['solution'])
    else:
        session['current_enigma'] = enigmas[currentEnigma-1]
        return render_template('enigmas/game.html'
                               , current_enigma=currentEnigma
                               , enigma=session['current_enigma']['description']
                               , hint=session['current_enigma']['hint']
                               , solution=session['current_enigma']['solution'])
