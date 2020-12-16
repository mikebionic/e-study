from flask import Flask, render_template

from . import bp


@bp.route("/courses")
def courses():
	return render_template("courses.html")