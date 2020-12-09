from ..db import db


class Client(db.Model):
	__tablename__ = "clients"

	id = db.Column(db.Integer, primary_key=True)

	name = db.Column(db.String, nullable=False)
	surname = db.Column(db.String, nullable=False)

