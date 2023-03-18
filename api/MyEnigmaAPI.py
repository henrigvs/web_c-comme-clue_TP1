from flask import Flask, jsonify, request
from controller.EnigmaController import EnigmaController
from controller.EnigmaService import EnigmaService
from domain.EnigmaRepository import EnigmaRepository

app = Flask(__name__)
enigmaRepository = EnigmaRepository()
enigmaService = EnigmaService(enigmaRepository)
enigmaController = EnigmaController(enigmaService)


@app.route('/enigmas', methods=['GET'])
def get_all_enigmas():
    enigmas = enigmaController.getAllEnigmas()
    return jsonify(enigmas)


@app.route('/enigmas', methods=['POST'])
def add_enigma():
    data = request.get_json()
    enigmaController.addEnigma(data['name'], data['description'], data['solution'])
    return jsonify({'success': True}), 201


if __name__ == '__main__':
    app.run(debug=True)
