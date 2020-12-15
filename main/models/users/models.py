from main import db, login_manager
from datetime import datetime
from flask_login import UserMixin
from main.models.main.models import UpdatesInfo

@login_manager.user_loader
def load_user(UserId):
	return Users.query.get(int(UserId))


class Users(UpdatesInfo,db.Model,UserMixin):
	__tablename__="tbl_me_users"
	UserId = db.Column(db.Integer,nullable=False,primary_key=True)
	UserFullName = db.Column(db.String(100))
	UserName = db.Column(db.String(60),nullable=False)
	UserEmail = db.Column(db.String(100),unique=True)
	UserPassword = db.Column(db.String(60),nullable=False)
	UserCode = db.Column(db.String(100),unique=True)
	UserTypeId = db.Column(db.Integer,db.ForeignKey("tbl_me_user_type.UserTypeId"))
	# Image = db.relationship('Image',backref='users',lazy=True)
	# Courses = db.relationship('Courses',backref='users',lazy=True)
	# Favorites = db.relationship('Favorites',backref='users',lazy=True)
	# Bookmarks = db.relationship('Bookmarks',backref='users',lazy=True)
	
	def is_admin(self):
		return self.UserTypeId == 1

	def get_id(self):
		return (self.UserId)

	def update(self, **kwargs):
		for key, value in kwargs.items():
			if value is not None:
				if hasattr(self, key):
					setattr(self, key, value)

	def to_json(self):
		json_data = {
			"UserId": self.UserId,
			"UserFullName": self.UserFullName,
			"UserName": self.UserName,
			"UserEmail": self.UserEmail,
			"UserPassword": self.UserPassword,
			"UserCode": self.UserCode,
			"UserTypeId": self.UserTypeId
		}
		return json_data


class User_type(UpdatesInfo,db.Model,UserMixin):
	__tablename__="tbl_me_user_type"
	UserTypeId = db.Column(db.Integer,nullable=False,primary_key=True)
	UserTypeName = db.Column(db.String(60),nullable=False)
	UserTypeInfo = db.Column(db.String(100),unique=True)
	Users = db.relationship('Users',backref='user_type',lazy=True)

	def to_json(self):
		json_data = {
			"UserTypeId": self.UserTypeId,
			"UserTypeName": self.UserTypeName,
			"UserTypeInfo": self.UserTypeInfo
		}
		return json_data