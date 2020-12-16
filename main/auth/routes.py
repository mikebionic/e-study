from flask import render_template,url_for,session,flash,redirect,request
from flask_login import login_user,current_user,logout_user

from . import bp

from main.config import Config
from main import db,bcrypt,babel,gettext,lazy_gettext
from main.auth.forms import (
	LoginForm)
from main.models.user.models import User,Rp_acc


@bp.route("/login",methods=['GET','POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('main.main'))
	
	form = LoginForm()

	if form.validate_on_submit(): 
		user = User.query.filter_by(UEmail=form.email.data).first()
		if user and bcrypt.check_password_hash(user.UPass,form.password.data):
			login_user(user, remember = form.remember.data)
			next_page = request.args.get("next")
			return redirect(next_page) if next_page else redirect(url_for('main.main'))
		else:
			flash(lazy_gettext('Login Failed! Check credentials'),'danger')
	
	return render_template(
		f"{Config.COMMERCE_TEMPLATES_FOLDER_PATH}/auth/login.html",
		title = gettext('Login'),
		form = form)


@bp.route("/logout")
def logout():
	logout_user()
	return redirect(url_for('main.main'))

