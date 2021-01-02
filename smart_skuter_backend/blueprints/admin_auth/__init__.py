from flask import Blueprint

from smart_skuter_backend.blueprints.admin_auth.login_page import login, logout

admin_auth_bp = Blueprint("admin_auth", __name__)

admin_auth_bp.add_url_rule("/login", methods=("GET", "POST"), view_func=login)
admin_auth_bp.add_url_rule("/logout", view_func=logout)
