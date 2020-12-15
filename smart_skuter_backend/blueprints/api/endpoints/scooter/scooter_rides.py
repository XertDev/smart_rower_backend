from flask_restful import Resource, abort
from sqlalchemy import exc

from smart_skuter_backend import db
from smart_skuter_backend.model import Ride


class ScooterRidesEndpoint(Resource):
	def get(self, scooter_id):
		"""
		List of rides for scooter
		---
		parameters:
			-
				name: scooter_id
				in: path
				schema:
					type: integer
				example: 0
				required: true
				description: Which scooter ride to display for?
		responses:
			200:
				description: Scooter's rides
				content:
					application/json:
						schema:
							type: object
							properties:
								ride_ids:
									type: array
									items:
										type: integer

						example: {"ride_ids": [0, 2, 3]}
			404:
				description: Scooter not found
				content:
					application/json:
						schema:
							type: object
							properties:
								status:
								type: string
						example: {"status": "Scooter id=0 does not exist"}
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
			# todo: with entities?
			scooter_exist = db.session.query(db.exists().where(Ride.scooter_id == scooter_id)).scalar()
			if scooter_exist:
				return {
					"ride_ids": db.query(Ride.id).filter(Ride.scooter_id == scooter_id).all()
				}
			else:
				abort(404, status="Scooter id={} does not exist".format(scooter_id))
		except exc.SQLAlchemyError:
			abort(500, status="Internal error")

