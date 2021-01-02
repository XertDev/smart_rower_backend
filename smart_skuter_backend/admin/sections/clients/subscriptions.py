from flask_babelex import lazy_gettext
from wtforms import PasswordField

from smart_skuter_backend.admin.views.LTEModelView import LTEModelView
from smart_skuter_backend.db import db
from smart_skuter_backend.model import ClientSubscription


class SubscriptionsView(LTEModelView):
	def __init__(self):
		super().__init__(
			ClientSubscription,
			db.session,
			name=lazy_gettext("Subscriptions"),
			category=lazy_gettext("Clients"),
			menu_icon_type="fa",
			menu_icon_value="fa-user"
		)

	can_export = True
	export_types = ["csv", "json", "xml", "xls"]
	can_set_page_size = True

	column_list = [
		"client",
		"start_time",
		"end_time",
	]

	form_columns = [
		"client",
		"start_time",
		"end_time",
	]

