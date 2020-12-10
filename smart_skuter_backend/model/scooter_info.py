from ..db import db
from geoalchemy2 import Geometry


class ScooterInfo(db.Model):
	__tablename__ = "scooter_info"

	timestamp = db.Column(db.TIMESTAMP, primary_key=True)
	scooter_id = db.Column(db.Integer, db.ForeignKey("scooters.id"))
	
	battery_level = db.Column(db.Integer, nullable=False)
	location = db.Column(Geometry("Point"), nullable=False)
	engine_power = db.Column(db.Integer, nullable=False)


  # zbior lokacji -> trasa
  # trasa zapisywana u klienta


