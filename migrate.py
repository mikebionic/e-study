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

from db_migrate_data.default_data import user_types, education_groups
from db_migrate_data.test_user_data import users
# from db_migrate_data.test_edu_data import 

db.drop_all()
db.create_all()

for user_type in user_types:
	db.session.add(User_type(**user_type))

for user in users:
	db.session.add(User(**user))

for education_group in education_groups:
	db.session.add(Education_group(**education_group))


db.session.commit()