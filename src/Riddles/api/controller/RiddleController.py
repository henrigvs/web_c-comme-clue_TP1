from flask import jsonify, request, Blueprint

from src.Riddles.api.service.RiddleService import RiddleService
from src.Riddles.domain.Riddle import Riddle
from src.Riddles.domain.RiddleRepository import RiddleRepository

# Blueprint
riddleBP = Blueprint('riddles', __name__)

# Initializing of service
riddleRepository = RiddleRepository()
riddleService = RiddleService(riddleRepository)

# Create initial data
riddleRepository.addRiddle(Riddle("Qu'est-ce qui est jaune et qui attend", "jonathan", "pas d'indice", 0))
riddleRepository.addRiddle(Riddle("Je mets mes dents entre tes dents", "fourchette", "Je suis un couvert de table", 1))
riddleRepository.addRiddle(Riddle("Même en marchant vers lui, vous ne pourrez jamais l'atteindre", "horizon",
                           "On peut me voir à la plage", 1))


# POST
@riddleBP.route('/', methods=['POST'])
def addEnigma():
    data = request.get_json()
    riddleService.addEnigma(data['description'], data['solution'], data['hint'], data['difficulty'])
    return jsonify({'success': True}), 201


# DELETE
@riddleBP.route('/<id>', methods=['DELETE'])
def deleteEnigma(id):
    riddleService.deleteEnigma(id)
    return jsonify({'success': True}), 200


# PUT
@riddleBP.route('/<id>', methods=['PUT'])
def updateEnigma(id):
    data = request.get_json()
    riddleService.updateEnigma(id, data['description'], data['solution'], data['hint'], data['difficulty'])
    return jsonify({'success': True}), 201


# GET
@riddleBP.route('/', methods=['GET'])
def getAllEnigmas():
    return jsonify(riddleService.getAllEnigmas())


@riddleBP.route('/<id>', methods=['GET'])
def getEnigmaById(id):
    return jsonify(riddleService.getEnigmaById(id))
