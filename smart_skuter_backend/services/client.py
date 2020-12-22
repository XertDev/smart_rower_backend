from flask_login import login_user
from sqlalchemy import exc
from werkzeug.exceptions import abort

from smart_skuter_backend.exceptions import AlreadyExistError
from ..db import db
from ..model import Client


def authenticate(email: str, password: str) -> bool:
	try:
		client = db.session.query(Client)\
			.filter_by(email=email)\
			.first()

		if not client:
			return False

		if not client.check_password(password):
			return False

		login_user(client)
		return True

	except exc.SQLAlchemyError:
		raise RuntimeError("Internal error")


def register(email, name, surname, password):
	client = Client()
	client.email = email
	client.name = name
	client.surname = surname
	client.set_password(password)
	if db.session.query(db.exists().where(Client.email == email)).scalar():
		raise AlreadyExistError("User already exist")
	try:
		db.session.add(client)
		db.session.commit()
	except exc.SQLAlchemyError:
		raise RuntimeError("Internal error")
