from flask_restful import fields

scooter_with_status_fields = {
	"id": fields.Integer,
	"state": fields.String,
	"latest_info": fields.Nested({
		"timestamp": fields.DateTime,
		"battery_level": fields.Integer
	})
}
