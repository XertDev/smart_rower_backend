from flask_restful import Resource, abort, marshal_with
from sqlalchemy import exc

from smart_skuter_backend.db import db
from smart_skuter_backend.model import Scooter, ScooterState
from ..fields import scooter_with_status_fields


class ScootersEndpoint(Resource):
	@marshal_with(scooter_with_status_fields)
	def get(self):
		"""
		List of all scooters
		---
		responses:
			200:
				description: Client succesfully authenticated
				content:
					application/json:
						schema:
							type: array
							items:
								$ref: '#/components/schemas/ScooterWithStatus'
						example: [{"id": 0, state: "AVAILABLE", latest_info: {timestamp: "Wed, 02 Oct 2002 15:00:00 +0200", battery_level: 100}}]
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
			return db.session.query(Scooter).all()
		except exc.SQLAlchemyError:
			abort(500, status="Internal error")

	@marshal_with(scooter_with_status_fields)
	def post(self):
		"""
		Create scooter
		---
		requestBody:
			content:
				application/json:
					schema:
						type: object
						properties:
							state:
								$ref: '#/components/schemas/ScooterState'
					example: {state: "AVAILABLE"}
		responses:
			201:
				description: Scooter created
				content:
					application/json:
						schema:
							$ref: '#/components/schemas/Scooter'
						example: {"id": 0, state: "AVAILABLE"}
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
		args = self.create_parser.parse_args()

		scooter = Scooter()
		scooter.state = ScooterState[args.state]
		db.session.add(scooter)
		try:
			db.session.commit()
			return scooter
		except exc.SQLAlchemyError:
			abort(500, status="Internal error")
