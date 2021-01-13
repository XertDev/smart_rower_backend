from ..db import db


class Ride(db.Model):
	__tablename__ = "rides"

	id = db.Column(db.Integer, primary_key=True)
	client_id = db.Column(db.Integer, db.ForeignKey("clients.id"), nullable=False)
	scooter_id = db.Column(db.Integer, nullable=False)

	start_time = db.Column(db.TIMESTAMP, nullable=False)
	end_time = db.Column(db.TIMESTAMP, nullable=True)

	kilometers_distance = db.Column(db.Float, nullable=False)
	pricing = db.Column(db.Float, nullable=False)

	checkpoints = db.relationship(
		"ScooterInfo",
		primaryjoin="and_("
			"Ride.scooter_id == ScooterInfo.scooter_id,"
			"between("
			"ScooterInfo.timestamp,"
			"Ride.start_time,"
			"Ride.end_time"
			")"
		")",
		uselist=True,
		viewonly=True
	)

	__table_args__ = (
		db.ForeignKeyConstraint([scooter_id, start_time], ["scooter_info.scooter_id", "scooter_info.timestamp"]),
		db.ForeignKeyConstraint([scooter_id, end_time], ["scooter_info.scooter_id", "scooter_info.timestamp"]),
		{}
	)

