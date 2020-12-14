from flask_restful import Resource, reqparse, abort

from smart_skuter_backend.blueprints.api.endpoints.validators import email, min_length
from smart_skuter_backend.services.client import register

parser = reqparse.RequestParser()
parser.add_argument(
	"name", dest="name",
	location="json", required=True,
)
parser.add_argument(
	"surname", dest="surname",
	location="json", required=True,
)
parser.add_argument(
	"email", dest="email",
	location="json", type=email, required=True,
)
parser.add_argument(
	"password", dest="password",
	location="json", type=min_length(8), required=True,
)


class SignUpEndpoint(Resource):
	def post(self):
		"""
		Client's sign up endpoint
		---
		requestBody:
			content:
				application/json:
					schema:
						type: object
						properties:
							name:
								type: string
							surname:
								type: string
							email:
								type: string
								format: email
							password:
								type: string
								format: password
								minLength: 8
						example:
							name: Joe
							surname: Doe
							email: joe.doe@example.com
							password: pa$$word
						required:
							- username
							- name
							- email
							- password
		responses:
			200:
				description: Client account succesfully created
				content:
					application/json:
						schema:
							type: object
							properties:
								status:
								type: string
							example: {"status": "Ok"}
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
		args = parser.parse_args()
		try:
			register(args.email, args.name, args.surname, args.password)
		except RuntimeError as e:
			abort(500, status="Internal error")
		return {"status": "Ok"}, 200
