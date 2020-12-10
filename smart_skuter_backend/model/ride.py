from ..db import db


class Ride(db.Model):
	__tablename__ = "rides"

	id = db.Column(db.Integer, primary_key=True)
	client_id = db.Column(db.Integer, db.ForeignKey("clients.id"), nullable=False)
	scooter_id = db.Column(db.Integer, db.ForeignKey("scooter_info.scooter_id"), nullable=False)

	start_time = db.Column(db.TIMESTAMP, db.ForeignKey("scooter_info.timestamp"), nullable=False)
	end_time = db.Column(db.TIMESTAMP, db.ForeignKey("scooter_info.timestamp"), nullable=True)

