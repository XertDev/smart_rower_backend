from flask import url_for
from flask_admin import AdminIndexView, expose
from flask_babelex import lazy_gettext
from flask_login import current_user
from werkzeug.utils import redirect

from smart_skuter_backend.model.client import ClientRole


class DashboardView(AdminIndexView):
	def __init__(self):
		super().__init__(
			name=lazy_gettext("Dashboard"),
			menu_icon_type="fa",
			menu_icon_value="fa-tachometer-alt"
		)

	def is_accessible(self):
		print(current_user.role)

		return current_user.is_authenticated and current_user.role == ClientRole.ADMIN

	def is_visible(self):
		return current_user.is_authenticated and current_user.role == ClientRole.ADMIN

	def inaccessible_callback(self, name, **kwargs):
		return redirect(url_for("admin_auth.login"))

	@expose("/")
	def index(self):
		return self.render(
			"pages/dashboard.html",
		)

