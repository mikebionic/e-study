from flask import Flask, jsonify, make_response

from . import bp


@bp.route("/educations/")
def educations():
	return make_response(jsonify({"data": "educations"}))


@bp.route("/majors/")
def majors():
	return make_response(jsonify({"data": "majors"}))


@bp.route("/courses/")
def courses():
	return make_response(jsonify({"data": "courses"}))


@bp.route("/library/")
def library():
	return make_response(jsonify({"data": "library"}))