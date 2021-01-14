from flask import url_for
from flask_admin import BaseView, expose
from flask_babelex import lazy_gettext
from flask_login import current_user
from werkzeug.utils import redirect

from smart_skuter_backend.db import db
from smart_skuter_backend.model import Scooter, ScooterState
from smart_skuter_backend.model.client import ClientRole


class ScooterMapView(BaseView):
	_template = "pages/custom/scooters_map.html"

	def __init__(self):
		super().__init__(
			name=lazy_gettext("Map"),
			category=lazy_gettext("Scooters"),
			menu_icon_type="fa",
			menu_icon_value="fa-map"
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
		scooters = db.session.query(Scooter).all()
		scooters_available = filter(lambda s: s.state==ScooterState.AVAILABLE, scooters)

		scooters_in_run = filter(lambda s: s.state==ScooterState.IN_RUN, scooters)
		scooters_unavailable = filter(lambda s: s.state==ScooterState.DISABLED, scooters)

		return self.render(
			self._template,
			scooters_available=scooters_available,
			scooters_unavailable=scooters_unavailable,
			scooters_in_run=scooters_in_run
		)
