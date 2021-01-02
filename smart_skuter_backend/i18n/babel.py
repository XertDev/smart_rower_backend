from flask import request, session
from flask_babelex import Babel

babel = Babel()


@babel.localeselector
def get_locale():
	if request.args.get('lang'):
		session['lang'] = request.args.get('lang')
	return session.get('lang', 'en')
