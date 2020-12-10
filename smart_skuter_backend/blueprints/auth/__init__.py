from flask import Blueprint, request, make_response, jsonify
from ...services import client

auth = Blueprint(
	"auth",
	__name__
)


@auth.route("/", methods=["post"])
def sign_in():
	data = request.form
	if "username" not in data or "password" not in data:
		return make_response(jsonify(status="error"), 200)

	if client.authenticate(data["username"], data["password"]):
		return make_response(jsonify(status="ok"), 200)
	return make_response(jsonify(status="invalid username or password"), 403)
