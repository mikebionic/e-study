import sys
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

class Config:
	SECRET_KEY = environ.get('SECRET_KEY')
	FLASK_ENV = 'development'
	DEBUG = True
	TESTING = True

	# POSTGRES_DB_URI = {
	#     'user': environ.get('POSTGRES_DB_USERNAME'),
	#     'pw': environ.get('POSTGRES_DB_PASSWORD'),
	#     'db': environ.get('POSTGRES_DB_DATABASE'),
	#     'host': environ.get('POSTGRES_DB_HOST'),
	#     'port': environ.get('POSTGRES_DB_PORT'),
	# }

	# SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES_DB_URI
	SQLALCHEMY_DATABASE_URI = 'sqlite:///estudy.db'
	SQLALCHEMY_ECHO = False

	MAIN_URL_PREFIX = '/study'

	# default language for session
	BABEL_DEFAULT_LOCALE = 'tk'

	# MAIL CONFIGURATION
	### testing ##
	MAIL_SUPPRESS_SEND = False
	MAIL_DEBUG = False
	### / testing /
	MAIL_SERVER = environ.get('MAIL_SERVER')
	MAIL_PORT = environ.get('MAIL_PORT')
	MAIL_USE_TLS = True
	# MAIL_USE_SSL = False
	MAIL_ADDRESS = environ.get('MAIL_ADDRESS')
	MAIL_PASSWORD = environ.get('MAIL_PASSWORD')
	# / MAIL CONFIGURATION /

	# set to True if you want to use BCrypt hashing
	HASHED_PASSWORDS = False

	# IMAGES CONFIGURATION 
	# icon extentions and size
	ALLOWED_ICON_EXTENSIONS = set(['png','jpg','jpeg','svg'])
	ALLOWED_IMAGE_EXTENSIONS = set(['png','jpg','jpeg'])
	MAX_CONTENT_LENGTH = 16 * 1024 * 1024
	IMAGE_RANDOM_HEX_LENGTH = 14

	# Characters that are unable to use in FileName
	FILENAME_INVALID_CHARACTERS = ['/', '\\', '"', ':', '*', '?', '<', '>', '|']

	# VIEW AND ROUTES CONFIGURATION\
	COMMERCE_HOME_PAGE = "/commerce"

	# / VIEW AND ROUTES CONFIGURATION /

	# view route titles configuration
	# Info to be displayed in html: <title>Home page</title>
	# set to None if dont want to display anything 
	COMMERCE_HOME_PAGE_TITLE = environ.get('COMMERCE_HOME_PAGE_TITLE') if environ.get('COMMERCE_HOME_PAGE_TITLE') else "Main"
	COMMERCE_ABOUT_PAGE_TITLE = "About us"
