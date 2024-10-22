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

	battery_model = db.Column(db.String, nullable=False)
	mac = db.Column(db.Integer, nullable=False)
	vehicle_type = db.Column(db.Integer, nullable=False)

	info_history = db.relationship("ScooterInfo", order_by="desc(ScooterInfo.actual_time)", lazy="dynamic")
	latest_info = db.relationship("ScooterInfo", order_by="desc(ScooterInfo.actual_time)", uselist=False, lazy=False)
