from flask_login import LoginManager

from ..db import db
from ..model import Client


login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
	return db.session.query(Client).filter_by(id=user_id).first()
