# -*- coding: utf-8 -*-
from flask import Flask,session,request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from babel import numbers,dates
from datetime import date,datetime,time
from flask_babel import Babel,format_date,gettext,lazy_gettext
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from flask_wtf.csrf import CSRFProtect
from flask_cors import CORS

from main_pack.config import Config

login_manager = LoginManager()
sess = Session()
bcrypt = Bcrypt()
babel = Babel()
db = SQLAlchemy()
csrf = CSRFProtect()

login_manager.login_view = 'auth.login'
login_manager.login_message = lazy_gettext('Login to get your classes!')
login_manager.login_message_category = 'info'

@babel.localeselector
def get_locale():
	try:
		language = session['language']
	except KeyError:
		session['language'] = 'tk'
		language = session['language']
	if language is not None:
		return language
	return 'tk'

LANGUAGES = {
	'en': 'English',
	'tk': 'Turkmen',
	'ru': 'Russian'
}

def create_app(config_class=Config):
	app = Flask(__name__, static_url_path='/static')
	app.config.from_object(Config)
	
	CORS(app)

	db.init_app(app)
	login_manager.init_app(app)
	babel.init_app(app)
	mail.init_app(app)
	csrf.init_app(app)
	sess.init_app(app)

	main_url_prefix = app.config.get('MAIN_URL_PREFIX')
	admin_url_prefix = app.config.get('ADMIN_URL_PREFIX')

	# from main_pack.models import bp as models_bp
	# app.register_blueprint(models_bp)

	# from main_pack.main import bp as main_bp
	# app.register_blueprint(main_bp,url_prefix=main_url_prefix)

	# from main.auth import bp as auth_bp
	# app.register_blueprint(auth_bp,url_prefix=main_url_prefix)

	# from main.users import bp as users_bp
	# app.register_blueprint(users_bp,url_prefix=main_url_prefix)

	# from main.admin import bp as admin_bp
	# app.register_blueprint(admin_bp,url_prefix=admin_url_prefix)

	return app