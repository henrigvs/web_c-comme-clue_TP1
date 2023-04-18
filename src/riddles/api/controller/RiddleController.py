from flask import jsonify, request, Blueprint

from src.Riddles.api.service.RiddleService import RiddleService
from src.Riddles.api.service.dtos.CreateRiddleDTO import CreateRiddleDTO
from src.Riddles.api.service.dtos.RiddleDTO import RiddleDTO
from src.Riddles.domain.Riddle import Riddle
from src.Riddles.domain.RiddleRepository import RiddleRepository

# Blueprint
riddleBP = Blueprint('riddles', __name__)

# Initializing of service
riddleRepository = RiddleRepository()
riddleService = RiddleService(riddleRepository)


# POST
@riddleBP.route('/addRiddle', methods=['POST'])
def addRiddle():
    data = request.get_json()
    createRiddleDTO = CreateRiddleDTO(data['description'], data['solution'], data['clue'], data['difficulty'], data['ownerId'])
    riddleDTO = riddleService.addRiddle(createRiddleDTO)
    return _jsonifyRiddles(riddleDTO, 201, "add riddle failed", 400)


# DELETE
@riddleBP.route('/delete/<riddleId>', methods=['DELETE'])
def deleteRiddle(riddleId):
    riddleDTO = riddleService.deleteRiddle(riddleId)
    return _jsonifyRiddles(riddleDTO, 200, "riddleId unknown", 404)


# PUT
@riddleBP.route('/edit/<riddleId>', methods=['PUT'])
def editRiddle(riddleId):
    data = request.get_json()
    createRiddleDTO = CreateRiddleDTO(data['description'], data['solution'], data['clue'], data['difficulty'], data['ownerId'])
    riddleDTO = riddleService.editRiddle(createRiddleDTO, riddleId)
    return _jsonifyRiddles(riddleDTO, 200, "riddleId unknown", 404)


# GET
@riddleBP.route('/getAllRiddles', methods=['GET'])
def getAllRiddles():
    riddleDTOs = riddleService.getAllRiddle()
    return jsonify([riddleDTO.to_dict() for riddleDTO in riddleDTOs])


@riddleBP.route('/riddle/<riddleId>', methods=['GET'])
def getRiddleById(riddleId):
    riddleDTO = riddleService.getRiddleByID(riddleId)
    return _jsonifyRiddles(riddleDTO, 200, "riddleId unknown", 404)


def _jsonifyRiddles(riddleDTO: RiddleDTO, code_ok: int, message_ko, code_ko: int):
    if riddleDTO is not None:
        return jsonify(riddleDTO.to_dict()), code_ok
    else:
        return jsonify({'success': False, 'message': message_ko}), code_ko


# Create initial data
riddleRepository.addRiddle(Riddle(
    "Qu'est-ce qui est jaune et qui attend",
    "jonathan",
    "pas d'indice",
    0,
    "owner id 1"))
riddleRepository.addRiddle(Riddle(
    "Je mets mes dents entre tes dents",
    "fourchette",
    "Je suis un couvert de table",
    1,
    "owner id 1"))
riddleRepository.addRiddle(Riddle(
    "Même en marchant vers lui, vous ne pourrez jamais l'atteindre",
    "horizon",
    "On peut me voir à la plage",
    1,
    "owner id 1"))
riddleRepository.addRiddle(Riddle(
    "Mon premier s'accroche aux arbres. Mon deuxième est le contraire de rapide. Mon troisième est le contraire de matin. Mon tout s'accroche aux branches des arbres",
    "Balançoire",
    "Bas - Lent - Soir",
    3,
    "1"))
riddleRepository.addRiddle(Riddle(
    "On me voit une fois dans la journée, une fois dans la nuit et deux fois dans l'année",
    "N",
    "Je suis une lettre",
    2,
    "owner id 1"))
riddleRepository.addRiddle(Riddle(
    "Je vole même si je n'ai pas d'aile",
    "Temps",
    "On peut essayer de courrir contre lui",
    3,
    "owner id 1"))
riddleRepository.addRiddle(Riddle(
    "Même si je fais mon travail, je suis toujours insulté",
    "Réveil-matin",
    "Je suis la première chose qu'on entend en se réveillant",
    1,
    "owner id 1"))
riddleRepository.addRiddle(Riddle(
    "Qu'est-ce qui peut être dans la mer et dans le ciel?",
    "Etoile",
    "Je brille par nuit claire",
    1,
    "owner id 1"))
riddleRepository.addRiddle(Riddle(
    "Qu'est-ce qui fait le tour de la maison sans bouger ?",
    "Mur",
    "Je suis souvent fait de briques",
    1,
    "owner id 1"))
