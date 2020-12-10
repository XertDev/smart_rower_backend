import enum

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from ..db import db


class ClientRole(enum.Enum):
	ADMIN = "ADMIN"
	NORMAL = "NORMAL"


class Client(db.Model, UserMixin):
	__tablename__ = "clients"

	id = db.Column(db.Integer, primary_key=True)

	role = db.Column(db.Enum(ClientRole), nullable=False, default=ClientRole.NORMAL)
	username = db.Column(db.String, nullable=False)
	name = db.Column(db.String, nullable=False)
	surname = db.Column(db.String, nullable=False)
	login = db.Column(db.String, nullable=False)
	password_hash = db.Column(db.String, nullable=False)

	start_account_date = db.Column(db.TIMESTAMP, nullable=False)

	subscriptions_history = db.relationship("ClientSubscription", order_by="desc(ClientSubscription.end_time)", lazy="dynamic")

	rides = db.relationship("Ride", lazy="selectin")

	def set_password(self, password: str) -> None:
		self.password_hash = generate_password_hash(password)

	def check_password(self, password: str) -> bool:
		return check_password_hash(self.password_hash, password)

	def get_id(self):
		return self.id

