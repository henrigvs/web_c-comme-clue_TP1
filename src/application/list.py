from src.application.static_methods.Pagination import Pagination
from src.application.static_methods.JSONGetter import JSONGetter

from flask import Blueprint, render_template, session

listBP = Blueprint('list', __name__)
difficultyLevel = 0
enigmasByPage = 5
currentPage = 0
perPage = 5


@listBP.route('/', methods=['GET'])
@listBP.route('/<int:page>', methods=['GET'])
def list(page=1):
    global perPage

    if session.get('userIsConnected') is None:
        userConnected = False
    else:
        userConnected = True

    enigmas = JSONGetter.getEnigmasJSON()
    enigmasPaginated = Pagination.paginateEnigmas(enigmas, perPage)
    totalPages = int((len(enigmas) + perPage - 1) / perPage)

    if page > totalPages or page < 1:
        return render_template('error/404.html'), 404

    return render_template('enigmas/list.html'
                           , enigmas=enigmasPaginated[page]
                           , difficultyLevel=None
                           , currentPage=page
                           , totalPages=totalPages
                           , userConnected=userConnected)
