from ..db import db
from geoalchemy2 import Geometry


class ScooterInfo(db.Model):
	__tablename__ = "scooter_info"

	actual_time = db.Column(db.TIMESTAMP, primary_key=True)
	scooter_id = db.Column(db.Integer, db.ForeignKey("scooters.id"), primary_key=True)
	
	location = db.Column(Geometry("Point"), nullable=False)
	location_x = db.column_property(location.ST_X())
	location_y = db.column_property(location.ST_Y())

	battery_level = db.Column(db.Float, nullable=False)
	battery_temp = db.Column(db.Float, nullable=False)
	battery_cycle = db.Column(db.Integer, nullable=False)
	is_charging = db.Column(db.Boolean, nullable=False)
	is_locked = db.Column(db.Boolean, nullable=False)
	is_riding = db.Column(db.Boolean, nullable=False)
	reversed_by = db.Column(db.Integer, nullable=True)
	ready_to_ride = db.Column(db.Boolean, nullable=False)
	zone_id = db.Column(db.Integer, nullable=False)


  # zbior lokacji -> trasa
  # trasa zapisywana u klienta


