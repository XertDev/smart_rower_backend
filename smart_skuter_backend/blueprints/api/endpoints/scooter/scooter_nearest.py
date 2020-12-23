from flask_restful import Resource, reqparse, marshal_with, abort
from sqlalchemy import exc, func

from smart_skuter_backend.blueprints.api.endpoints.fields import scooter_with_status_fields, scooter_distance_fields
from smart_skuter_backend.db import db
from smart_skuter_backend.model import Scooter, ScooterState, ScooterInfo


class ScooterNearestEndpoint(Resource):
	create_parser = reqparse.RequestParser()
	create_parser.add_argument(
		"location_x", dest="location_x",
		location="json", type=float, required=True,
	)
	create_parser.add_argument(
		"location_y", dest="location_y",
		location="json", type=float, required=True,
	)
	create_parser.add_argument(
		"distance", dest="distance",
		location="json", type=float, required=True,
	)
	create_parser.add_argument(
		"only_available", dest="only_available",
		location="json", type=bool, required=False,
		default=False
	)
	# todo: get or post?
	@marshal_with(scooter_distance_fields)
	def post(self):
		"""
		List of nearest scooters
		---
		requestBody:
			content:
				application/json:
					schema:
						type: object
						properties:
							location_x:
								type: float
							location_y:
								type: float
							distance:
								type: float
							only_available:
								type: bool
								required: false
								default: false
					example: {location_x: 3, location_y: 4, distance: 4.5, only_available: false}
		responses:
			200:
				description: List of nearest scooters
				content:
					application/json:
						schema:
							type: array
							items:
								type: object
								properties:
									scooter:
										$ref: '#/components/schemas/ScooterWithStatus'
									distance:
										type: float
						example: [{"scooter":{"id": 0, state: "AVAILABLE", latest_info: {timestamp: "Wed, 02 Oct 2002 15:00:00 +0200", battery_level: 100}},"distance":3.4}]
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
		x = args.location_x
		y = args.location_y
		distance_limit = args.distance

		query = """
			select
				scooters.id as scooters_id,
				scooters.state as scooters_state,
				ST_Distance(scooter_info.location, 'POINT(:x :y)') as distance,
				ST_X(scooter_info.location) as "scooter_info_location_x",
				ST_Y(scooter_info.location) as "scooter_info_location_y",
				scooter_info.timestamp as scooter_info_timestamp,
				scooters.id as scooter_info_scooter_id,
				ST_AsEWKB(scooter_info.location) as scooter_info_location,
				scooter_info.battery_level as scooter_info_battery_level
			from scooters
			join lateral (
				select
					scooter_info.location as location,
					scooter_info.timestamp as timestamp,
					scooter_info.scooter_id as scooter_id,
					scooter_info.battery_level as battery_level
				from scooter_info
				where scooters.id = scooter_info.scooter_id
				order by scooter_info.timestamp desc
				fetch first 1 row only
				) as scooter_info on scooter_info.scooter_id = scooters.id
			where ST_Distance(scooter_info.location, 'POINT(:x :y)') <= :dist
		"""
		if args.only_available:
			query += "and scooters.state = 'AVAILABLE'\n"
		query += "order by distance asc"

		try:
			scooters_with_dist = db.session.query(Scooter, "distance").from_statement(db.text(query))\
				.params(x=x, y=y, dist=distance_limit)\
				.options(db.contains_eager(Scooter.latest_info))\
				.all()

			return[
				{
					"scooter": entry[0],
					"distance": entry[1]
				}
				for entry in scooters_with_dist
			]
		except exc.SQLAlchemyError:
			abort(500, status="Internal error")
