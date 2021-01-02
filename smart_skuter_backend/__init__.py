from flasgger import Swagger
from flask import Flask


def create_app(config=None):
	app = Flask(
		__name__,
		instance_relative_config=True,
		template_folder="template"
	)

	app.config.from_mapping(
		SECRET_KEY="dev"
	)

	app.config.from_object("config")
	app.config.from_pyfile("config.py", silent=True)
	app.jinja_options['extensions'].append('jinja2.ext.do')

	from .db import db
	from . import model
	db.init_app(app)

	from .login_manager import login_manager
	login_manager.init_app(app)

	from .blueprints.api import api_blueprint
	app.register_blueprint(api_blueprint)

	from .blueprints.admin_auth import admin_auth_bp
	app.register_blueprint(admin_auth_bp)

	from .admin import admin
	admin.init_app(app)

	from .i18n.babel import babel
	babel.init_app(app)

	swagger = Swagger(app)
	return app
