from flask import jsonify, request, Blueprint
from Enigmas.api.controller.EnigmaController import EnigmaController
from Enigmas.api.controller.EnigmaService import EnigmaService
from Enigmas.domain.EnigmaRepository import EnigmaRepository

enigmaBP = Blueprint('enigma', __name__)
enigmaRepository = EnigmaRepository()
enigmaService = EnigmaService(enigmaRepository)
enigmaController = EnigmaController(enigmaService)

# Initializing some Enigmas
enigmaController.addEnigma("Qu'est-ce qui est jaune et qui attend", "jonathan", "pas d'indice")
enigmaController.addEnigma("Je mets mes dents entre tes dents", "fourchette", "Je suis un couvert de table")
enigmaController.addEnigma("Même en marchant vers lui, vous ne pourrez jamais l'atteindre", "horizon",
                           "On peut me voir à la plage")


@enigmaBP.route('/', methods=['POST'])
def addEnigma():
    data = request.get_json()
    enigmaController.addEnigma(data['description'], data['solution'], data['hint'])
    return jsonify({'success': True}), 201


@enigmaBP.route('/', methods=['GET'])
def getAllEnigmas():
    return jsonify(enigmaController.getAllEnigmas())


@enigmaBP.route('/<id>', methods=['GET'])
def getEnigmaById(id):
    return jsonify(enigmaController.getEnigmaById(int(id)))
