from flask import Blueprint, request, render_template, session
import requests

import app
from src.application.static_methods import JSONToERiddles

gameBP = Blueprint('game', __name__)
pointer = 1


def getRiddleJSON():    # Retrieve list of riddles from the getAllRiddles endpoint
    riddlesResponse = requests.get(f"http://localhost:{app.PORT}/riddles/getAllRiddles")
    riddles = JSONToERiddles.convertJSONToERiddlesArray(riddlesResponse.json())
    return riddles


def getNextRiddle(notCorrect):
    return render_template('riddles/game.html',
                           notCorrect=notCorrect,
                           currentRiddle=pointer,
                           riddle=session['currentRiddle'])


@gameBP.route('/', methods=['GET', 'POST'])
def game():
    global pointer
    riddles = getRiddleJSON()
    if request.method == 'POST':
        answer = request.form.get('answer').strip().lower()
        riddle = session['currentRiddle']

        if answer == riddle['solution'].lower():
            pointer += 1

            if pointer - 1 >= len(riddles):
                pointer = 1
                return render_template("riddles/game_completed.html")

            else:
                session['currentRiddle'] = riddles[pointer - 1]
                return getNextRiddle(notCorrect=False)

        else:
            return getNextRiddle(notCorrect=True)

    else:
        session['currentRiddle'] = riddles[pointer - 1]
        return getNextRiddle(notCorrect=False)
