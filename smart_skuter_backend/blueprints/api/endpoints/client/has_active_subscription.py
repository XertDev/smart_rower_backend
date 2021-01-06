from flask_restful import Resource, abort
from sqlalchemy import exc
from datetime import timedelta, datetime


from smart_skuter_backend.blueprints.api.endpoints.fields import ride_details
from smart_skuter_backend.db import db
from smart_skuter_backend.model import Client, Ride, ClientSubscription



class HasActiveSubscriptionEndpoint(Resource):
	def get(self, client_id):
		"""
		Does client have an active subscription 
		---
		parameters:
			-
				name: client_id
				in: path
				schema:
					type: integer
				example: 0
				required: true
		responses:
			200:
				description: Has active subscription
				content:
					application/json:
						schema:
							type: object
							properties:
								ride_ids:
									type: array
									items:
										type: integer

						example: True
			404:
				description: Client not found
				content:
					application/json:
						schema:
							type: object
							properties:
								status:
								type: string
						example: {"status": "Client id=0 does not exist"}
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
			client_exist = db.session.query(db.exists().where(ClientSubscription.client_id == client_id)).scalar()
			if client_exist:
				client_subs = db.session.query(ClientSubscription).filter(ClientSubscription.client_id == client_id).all()

				for row in client_subs:
					if row.end_time > datetime.now():
						return True

				return False
            
            
			else:
				abort(404, status="Client id={} does not exist".format(client_id))
		except exc.SQLAlchemyError:
			abort(500, status="Internal error")
