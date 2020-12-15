from ..db import db


class Ride(db.Model):
	__tablename__ = "rides"

	id = db.Column(db.Integer, primary_key=True)
	client_id = db.Column(db.Integer, db.ForeignKey("clients.id"), nullable=False)
	scooter_id = db.Column(db.Integer, nullable=False)

	start_time = db.Column(db.TIMESTAMP, nullable=False)
	end_time = db.Column(db.TIMESTAMP, nullable=True)

	__table_args__ = (
		db.ForeignKeyConstraint([scooter_id, start_time], ["scooter_info.scooter_id", "scooter_info.timestamp"]),
		db.ForeignKeyConstraint([scooter_id, end_time], ["scooter_info.scooter_id", "scooter_info.timestamp"]),
		{}
	)

