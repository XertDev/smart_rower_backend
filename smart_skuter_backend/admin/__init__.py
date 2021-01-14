from flask_admin import Admin

from smart_skuter_backend.admin.sections import dashboard_view, clients_view, scooters_view
from smart_skuter_backend.admin.sections import subscriptions_view, scooters_map_view

admin = Admin(
	name="Skuter Z.O.O",
	base_template="pages/admin/base.html",
	template_mode='bootstrap3',
	index_view=dashboard_view,
	category_icon_classes={
	}
)

admin.add_view(clients_view)
admin.add_view(scooters_view)
admin.add_view(subscriptions_view)
admin.add_view(scooters_map_view)

