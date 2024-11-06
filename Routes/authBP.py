from flask import Blueprint
from Controllers import authController

auth_blueprint = Blueprint('auth_blueprint',__name__)
auth_blueprint.route('/register',methods=['POST'])(authController.register)