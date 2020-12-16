from flask import Flask, render_template

from . import bp


@bp.route("/")
@bp.route("/main")
def main():
	return render_template("main.html")