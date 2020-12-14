from flask_restful import Resource, abort, marshal_with, reqparse
from sqlalchemy import exc

from smart_skuter_backend import db
from smart_skuter_backend.blueprints.api.endpoints.fields import scooter_with_status_fields
from smart_skuter_backend.blueprints.api.endpoints.validators import enum_member
from smart_skuter_backend.model import Scooter, ScooterState


class ScooterEndpoint(Resource):
	@marshal_with(scooter_with_status_fields)
	def get(self, scooter_id):
		"""
		Details of scooter
		---
		parameters:
			-
				name: scooter_id
				in: path
				schema:
					type: integer
				example: 0
				required: true
				description: Which scooter to display?
		responses:
			200:
				description: Scooter found
				content:
					application/json:
						schema:
							$ref: '#/components/schemas/ScooterWithStatus'
						example: {"id": 0, state: "AVAILABLE", latest_info: {timestamp: "Wed, 02 Oct 2002 15:00:00 +0200", battery_level: 100}}
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
			scooter = db.session.query(Scooter).filter_by(id=scooter_id).first()
			if scooter:
				abort(404, status="Scooter id={} does not exist".format(scooter_id))

			return scooter
		except exc.SQLAlchemyError:
			abort(500, status="Internal error")

	create_parser = reqparse.RequestParser()
	create_parser.add_argument(
		"state", dest="state",
		location="json", type=enum_member(ScooterState), required=False,
		default="AVAILABLE"
	)
