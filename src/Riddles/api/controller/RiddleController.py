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

# Create initial data
riddleRepository.addRiddle(Riddle("Qu'est-ce qui est jaune et qui attend",
                                  "jonathan",
                                  "pas d'indice",
                                  0))
riddleRepository.addRiddle(Riddle("Je mets mes dents entre tes dents",
                                  "fourchette",
                                  "Je suis un couvert de table",
                                  1))
riddleRepository.addRiddle(Riddle("Même en marchant vers lui, vous ne pourrez jamais l'atteindre",
                                  "horizon",
                                  "On peut me voir à la plage",
                                  1))


# POST
@riddleBP.route('/addRiddle', methods=['POST'])
def addRiddle():
    data = request.get_json()
    createRiddleDTO = CreateRiddleDTO(data['description'], data['solution'], data['clue'], data['difficulty'])
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
    createRiddleDTO = CreateRiddleDTO(data['description'], data['solution'], data['clue'], data['difficulty'])
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
