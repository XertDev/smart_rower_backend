from flask_restful import Resource, abort, marshal_with
from sqlalchemy import exc

from smart_skuter_backend.blueprints.api.endpoints.fields import ride_details
from smart_skuter_backend.db import db
from smart_skuter_backend.model import Ride


class RideEndpoint(Resource):
	@marshal_with(ride_details)
	def get(self, ride_id):
		"""
		Details of ride
		---
		parameters:
			-
				name: ride_id
				in: path
				schema:
					type: integer
				example: 0
				required: true
				description: Which ride to display?
		responses:
			200:
				description: Ride found
				content:
					application/json:
						schema:
							$ref: '#/components/schemas/Ride'
						example: {"id": 1,"client_id": 2,"scooter_id": 1,"start_time": "Tue, 22 Dec 2020 18:46:00 -0000","end_time": "Tue, 22 Dec 2020 19:28:00 -0000","checkpoints": [{"timestamp": "Tue, 22 Dec 2020 18:46:00 -0000","battery_level": 10,"location_x": 1,"location_y": 2},{"timestamp": "Tue, 22 Dec 2020 19:20:00 -0000","battery_level": 10,"location_x": 1,"location_y": 3},{"timestamp": "Tue, 22 Dec 2020 19:28:00 -0000","battery_level": 10,"location_x": 1,"location_y": 4}]}
			404:
				description: Ride not found
				content:
					application/json:
						schema:
							type: object
							properties:
								status:
								type: string
						example: {"status": "Ride id=0 does not exist"}
			500:
				description: Internal error
				content:
					application/json:
						schema:
							type: object
							properties:
								status:
								type: string
						example: {"status": "Internal error"}
		"""
		try:
			ride = db.session.query(Ride).filter_by(id=ride_id).first()
			if not ride:
				abort(404, status="Ride id={} does not exist".format(ride_id))

			return ride
		except exc.SQLAlchemyError:
			abort(500, status="Internal error")


