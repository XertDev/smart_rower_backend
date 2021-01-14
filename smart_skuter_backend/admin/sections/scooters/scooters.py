from flask_babelex import lazy_gettext

from smart_skuter_backend.admin.views.LTEModelView import LTEModelView
from smart_skuter_backend.db import db
from smart_skuter_backend.model import  Scooter


class ScootersView(LTEModelView):
	def __init__(self):
		super().__init__(
			Scooter,
			db.session,
			name=lazy_gettext("Scooters"),
			category=lazy_gettext("Scooters"),
			menu_icon_type="fa",
			menu_icon_value="fa-user"
		)

	can_export = True
	export_types = ["csv", "json", "xml", "xls"]
	can_set_page_size = True

	column_labels = {
		"latest_info.location_x": "Pos X",
		"latest_info.location_y": "Pos Y",
		"latest_info.actual_time": "Timestamp",
		"latest_info.battery_level": "Battery level"

	}

	column_list = [
		"id",
		"state",
		"latest_info.actual_time",
		"latest_info.location_x",
		"latest_info.location_y",
		"latest_info.battery_level"
	]

	form_columns = [
		"state"
	]
