from flask import Flask, render_template

from . import bp


@bp.route("/library")
def library():
	return render_template("library.html")