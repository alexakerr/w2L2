from flask import Blueprint
from controllers.userController import login

loginblueprint = Blueprint("loginbp", __name__)

login_blueprint.route('/', methods=['POST'])(login)