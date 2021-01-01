from flask import Blueprint
from flask_restful import Api

from .endpoints import SignUpEndpoint, SignInEndpoint, ScootersEndpoint, ScooterEndpoint
from .endpoints import ScooterRidesEndpoint, RideEndpoint
from .endpoints import ClientRidesHistoryEndpoint
api_blueprint = Blueprint("api", __name__, )
api = Api(api_blueprint)

api.add_resource(SignUpEndpoint, "/client/signup")
api.add_resource(SignInEndpoint, "/client/signin")
api.add_resource(ScootersEndpoint, "/scooter")
api.add_resource(ScooterEndpoint, "/scooter/<int:scooter_id>")
api.add_resource(ScooterRidesEndpoint, "/scooter/<int:scooter_id>/rides")
api.add_resource(RideEndpoint, "/ride/<int:ride_id>")
api.add_resource(ClientRidesHistoryEndpoint, "/client/<int:client_id>/rides")
