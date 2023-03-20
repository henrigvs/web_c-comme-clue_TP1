from flask import Flask, request, render_template, redirect, flash

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Instanciation of a

# array of Enigmas
enigmas = {
    "Enigme 1 : Je mets mes dents entre tes dents! Qui suis-je ?": "fourchette",
    "Enigme 2 : Si tu me perds, tu tombes": "équilibre",
    "Enigme 3 : Même en marchant vers lui, vous ne pourrez jamais l'atteindre": "horizon",
    "Enigme 4": "answer4"
}

# array of hints
hints = {
    "Enigme 1 : Je mets mes dents entre tes dents! Qui suis-je ?": "Je suis un couvert de table",
    "Enigme 2 : Si tu me perds, tu tombes": "Plus le centre de gravité d'un objet est bas et plus je me renforce",
    "Enigme 3 : Même en marchant vers lui, vous ne pourrez jamais l'atteindre": "On me voit clairement en regardant la mer le long d'une plage",
    "Enigme 4": "hint4"
}

# Define the order of Enigmas
sequenceOfEnigma = ["Enigme 1 : Je mets mes dents entre tes dents! Qui suis-je ?",
                    "Enigme 2 : Si tu me perds, tu tombes",
                    "Enigme 3 : Même en marchant vers lui, vous ne pourrez jamais l'atteindre",
                    "Enigme 4"]

# index of current enigma
pointer = 0

# password for accessing the secret page
myPassword = "secret"


@app.route('/', methods=['GET', 'POST'])
def enigma():
    global pointer
    if request.method == 'POST':
        # User submits an answer
        answer = request.form['answer']
        # lower permits to transform all letters in lowercase
        correctAnswer = enigmas[sequenceOfEnigma[currentEnigma]].lower()

        if answer == correctAnswer:
            currentEnigma = currentEnigma + 1

            if currentEnigma < len(sequenceOfEnigma):
                return render_template('enigmas/enigma.html',
                                       enigma=sequenceOfEnigma[currentEnigma],
                                       hint=hints[sequenceOfEnigma[currentEnigma]])

            else:
                return render_template('end.html')

        else:
            return render_template('enigmas/enigma.html',
                                   enigma=sequenceOfEnigma[currentEnigma],
                                   hint=hints[sequenceOfEnigma[currentEnigma]],
                                   erreur=True)

    else:
        return render_template('enigmas/enigma.html',
                               enigma=sequenceOfEnigma[currentEnigma],
                               hint=hints[sequenceOfEnigma[currentEnigma]])
