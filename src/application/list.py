from src.application.static_methods.JSONGetter import JSONGetter
from src.application.static_methods.Pagination import Pagination

from flask import Blueprint, render_template, session

listBP = Blueprint('list', __name__)
difficultyLevel = 0
enigmasByPage = 5
currentPage = 0
perPage = 5


@listBP.route('/', methods=['GET'])
@listBP.route('/<int:page>', methods=['GET'])
def getList(page=1):
    global perPage

    if session.get('userIsConnected') is None:
        userConnected = False
    else:
        userConnected = True

    riddles = JSONGetter.getRiddlesJSON()
    riddlesPaginated = Pagination.paginateRiddle(riddles, perPage)
    totalPages = int((len(riddles) + perPage - 1) / perPage)

    if page > totalPages or page < 1:
        return render_template('error/404.html'), 404

    return render_template('riddles/list.html'
                           , riddles=riddlesPaginated[page]
                           , difficultyLevel=None
                           , currentPage=page
                           , totalPages=totalPages
                           , userConnected=userConnected)

