from flask_restful import Resource, abort
from sqlalchemy import exc

from smart_skuter_backend.db import db
from smart_skuter_backend.model import Client, ClientSubscription



class ClientSubscriptionHistoryEndpoint(Resource):
	def get(self, client_id):
		"""
		Client's subscription history
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
				description: Client's subscription history
				content:
					application/json:
						schema:
							type: object
							properties:
								subscription_ids:
									type: array
									items:
										type: integer

						example: {"subscription_ids": [0, 2, 3]}
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
				return {
					
					"subscription_ids": db.session.query(ClientSubscription.id).filter(ClientSubscription.client_id == client_id).all()
				}
			else:
				abort(404, status="Client id={} does not exist".format(client_id))
		except exc.SQLAlchemyError:
			abort(500, status="Internal error")
