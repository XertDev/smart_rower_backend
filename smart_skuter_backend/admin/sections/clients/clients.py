from flask_babelex import lazy_gettext
from wtforms import PasswordField

from smart_skuter_backend.admin.views.LTEModelView import LTEModelView
from smart_skuter_backend.db import db
from smart_skuter_backend.model import Client


class ClientView(LTEModelView):
	def __init__(self):
		super().__init__(
			Client,
			db.session,
			name=lazy_gettext("Clients"),
			category=lazy_gettext("Clients"),
			menu_icon_type="fa",
			menu_icon_value="fa-user"
		)

	can_export = True
	export_types = ["csv", "json", "xml", "xls"]
	can_set_page_size = True

	column_list = [
		"email",
		"name",
		"surname",
		"role",
		"start_account_date"
	]

	form_extra_fields = {
		"password": PasswordField("Password")
	}

	form_columns = [
		"email",
		"name",
		"surname",
		"role",
		"password",
		"start_account_date",
	]

	def on_model_change(self, form, model, is_created):
		if form.password.data is not None:
			model.set_password(form.password.data)
