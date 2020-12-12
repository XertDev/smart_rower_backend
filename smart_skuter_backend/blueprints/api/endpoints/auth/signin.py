from flask_restful import Resource, reqparse

from smart_skuter_backend.services.client import authenticate
from ..validators import email, min_length


parser = reqparse.RequestParser()
parser.add_argument(
	"email", dest="email",
	location="json", type=email, required=True,
)
parser.add_argument(
	"password", dest="password",
	location="json", type=min_length(8), required=True,
)


class SignIn(Resource):
	def post(self):
		"""
		Client's sign in endpoint
		---
		requestBody:
			content:
				application/json:
					schema:
						type: object
						properties:
							email:
								type: string
								format: email
							password:
								type: string
								format: password
								minLength: 8
						example:
							email: joe.doe@example.com
							password: pa$$word
						required:
							- email
							- password
		responses:
			200:
				description: Client succesfully authenticated
				content:
				 application/json:
					schema:
					type: object
					properties:
						status:
							type: string
					example: {"status": "Ok"}
				headers:
					Set-Cookie:
						schema:
							type: string
							example: session=abcde1234; Path=/; HttpOnly
			401:
				description: Internal error
				content:
					application/json:
						schema:
							type: object
							properties:
								status:
								type: string
						example: {"status": "Internal error"}
			500:
				description: Invalid username or password
				content:
					application/json:
						schema:
							type: object
							properties:
								status:
								type: string
						example: {"status": "Invalid username or password"}
		"""
		args = parser.parse_args()
		try:
			result = authenticate(args.email, args.password)
			if not result:
				return {"state": "Invalid username or password"}, 401
		except RuntimeError as e:
			return {"status": str(e)}, 500
		return {"state": "Ok"}, 200
