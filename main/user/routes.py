from flask import Flask, render_template

from . import bp


@bp.route("/user")
def user():
	return render_template("user.html")