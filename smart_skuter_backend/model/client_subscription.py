from ..db import db


class ClientSubscription(db.Model):
	__tablename__ = "client_subscriptions"

	id = db.Column(db.Integer, primary_key=True)
	client_id = db.Column(db.Integer, db.ForeignKey("clients.id"), nullable=False)

	start_time = db.Column(db.TIMESTAMP, nullable=False)
	end_time = db.Column(db.TIMESTAMP, nullable=False)

	client = db.relationship("Client", lazy="selectin", back_populates="subscriptions_history")
