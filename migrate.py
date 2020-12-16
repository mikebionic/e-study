from main import db, create_app

app = create_app()
app.app_context().push()

from main.models.user.models import User, User_type
from main.models.edu.models import (
	Education,
	Education_group,
	Faculty,
	Major,
	Subject,
	Course,
	Reference,
	Lesson,
	Reference,
	Hometask,
	Solution)

from db_migrate_data.default_data import user_types
from db_migrate_data.test_user_data import users 

db.drop_all()
db.create_all()

for user_type in user_types:
	db.session.add(User_type(**user_type))

for user in users:
	db.session.add(User(**user))


db.session.commit()