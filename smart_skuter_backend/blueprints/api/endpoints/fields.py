from flask_restful import fields


scooter_with_status_fields = {
	"id": fields.Integer,
	"state": fields.String,
	"latest_info": fields.Nested({
		"timestamp": fields.DateTime,
		"battery_level": fields.Integer
	}, default={})
}

ride_details = {
	"id": fields.Integer,
	"client_id": fields.Integer,
	"scooter_id": fields.Integer,
	"start_time": fields.DateTime,
	"end_time": fields.DateTime,
	"checkpoints": fields.List(fields.Nested({
		"timestamp": fields.DateTime,
		"battery_level": fields.Integer,
		"location_x": fields.Float,
		"location_y": fields.Float,
	}))
}
