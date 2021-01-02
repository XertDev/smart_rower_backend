from datetime import datetime

from flask import url_for
from flask_admin.contrib.sqla import ModelView
from flask_admin.model import typefmt
from flask_login import current_user
from werkzeug.utils import redirect

from smart_skuter_backend.model.client import ClientRole


def date_format(view, value):
	return value.strftime('%d.%m.%Y %H:%M:%S')


DEFAULT_FORMATTERS = dict(typefmt.BASE_FORMATTERS)
DEFAULT_FORMATTERS.update({datetime: date_format})

class LTEModelView(ModelView):
	list_template = "pages/admin/views/model/list.html"
	create_template = "pages/admin/views/model/create.html"
	edit_template = "pages/admin/views/model/edit.html"
	details_template = "pages/admin/views/model/details.html"

	def is_accessible(self):
		return current_user.is_authenticated and current_user.role == ClientRole.ADMIN

	def is_visible(self):
		return current_user.is_authenticated and current_user.role == ClientRole.ADMIN

	def inaccessible_callback(self, name, **kwargs):
		return redirect(url_for("login"))

	column_type_formatters = DEFAULT_FORMATTERS
