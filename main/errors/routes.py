from flask import make_response, jsonify, render_template, request
from main_pack.config import Config
from flask_wtf.csrf import CSRFError

from . import bp


@bp.app_errorhandler(400)
def bad_request(error):
	return render_template(f"{Config.COMMERCE_TEMPLATES_FOLDER_PATH}/errors/500.html"), 500


@bp.app_errorhandler(401)
def unauthorized(error):
	return render_template(f"{Config.COMMERCE_TEMPLATES_FOLDER_PATH}/errors/500.html"), 500


@bp.app_errorhandler(403)
def forbidden(error):
	return render_template(f"{Config.COMMERCE_TEMPLATES_FOLDER_PATH}/errors/403.html"), 403


@bp.app_errorhandler(404)
def not_found(error):
	return render_template(f"{Config.COMMERCE_TEMPLATES_FOLDER_PATH}/errors/404.html"), 404


@bp.app_errorhandler(405)
def method_not_found(error):
	return render_template(f"{Config.COMMERCE_TEMPLATES_FOLDER_PATH}/errors/405.html"), 405


@bp.app_errorhandler(410)
def gone(error):
	return render_template(f"{Config.COMMERCE_TEMPLATES_FOLDER_PATH}/errors/410.html"), 410


@bp.app_errorhandler(500)
def internal_server_error(error):
	return render_template(f"{Config.COMMERCE_TEMPLATES_FOLDER_PATH}/errors/500.html"), 500


@bp.app_errorhandler(CSRFError)
def handle_csrf_error(e):
	return {'status':'CSRFError','reason':e.description}, 400