from flask import request, render_template, redirect
from flask_babelex import gettext
from flask_login import current_user, logout_user

from smart_skuter_backend.model.client import ClientRole
from smart_skuter_backend.services.client import authenticate
from .form import LoginForm


def login():
	login_form = LoginForm(request.form)
	if "login" in request.form:
		email = request.form["email"]
		password = request.form["password"]
		if authenticate(email, password):
			return redirect("admin_auth")

		return render_template("pages/login.html", msg=gettext('Wrong user or password'), form=login_form)

	if not current_user.is_authenticated:
		return render_template("pages/login.html", form=login_form)

	if not current_user.role == ClientRole.ADMIN:
		return render_template("pages/login.html", msg=gettext('Only admin_auth can access admin_auth panel'), form=login_form)

	return redirect("admin")


def logout():
	logout_user()
	return redirect("login")
