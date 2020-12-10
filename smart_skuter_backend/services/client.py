from flask_login import login_user
from sqlalchemy import exc
from werkzeug.exceptions import abort

from ..db import db
from ..model import Client


def authenticate(username: str, password: str) -> bool:
	try:
		client = db.session.query(Client)\
			.filter_by(username=username)\
			.first()

		if not client:
			return False

		if not client.check_password(password):
			return False

		login_user(client)
		return True

	except exc.SQLAlchemyError:
		abort(500)

