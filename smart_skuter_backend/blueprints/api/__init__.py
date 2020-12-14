from flask import Blueprint
from flask_restful import Api

from .endpoints import SignUpEndpoint, SignInEndpoint, ScootersEndpoint, ScooterEndpoint

api_blueprint = Blueprint("api", __name__, )
api = Api(api_blueprint)

api.add_resource(SignUpEndpoint, "/client/signup")
api.add_resource(SignInEndpoint, "/client/signin")
api.add_resource(ScootersEndpoint, "/scooter")
api.add_resource(ScooterEndpoint, "/scooter/<int:scooter_id>")
