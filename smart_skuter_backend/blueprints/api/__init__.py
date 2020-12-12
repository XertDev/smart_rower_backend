from flask import Blueprint
from flask_restful import Api

from .endpoints import SignUp, SignIn

api_blueprint = Blueprint("api", __name__, )
api = Api(api_blueprint)

api.add_resource(SignUp, "/client/signup")
api.add_resource(SignIn, "/client/signin")
