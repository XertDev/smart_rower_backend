import enum

from ..db import db


class ScooterState(enum.Enum):
	AVAILABLE = "AVAILABLE"
	IN_RUN = "IN_RUN"
	DISABLED = "DISABLED"


class Scooter(db.Model):
	__tablename__ = "scooters"

	id = db.Column(db.Integer, primary_key=True)

	state = db.Column(db.Enum(ScooterState), nullable=False, default=ScooterState.AVAILABLE, server_default="AVAILABLE")
