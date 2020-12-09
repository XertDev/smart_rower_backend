import enum

from ..db import db

class ScooterState(enum.Enum):
	AVAILABLE = "AVAILABLE"

class Scooter(db.Model):
	__tablename__ = "scooter"

	id = db.Column(db.Integer)
