from flask import Flask, render_template

from . import bp


@bp.route("/admin")
def admin():
	return render_template("admin.html")