from main import db, create_app

app = create_app()
app.app_context().push()

from main.models.users.models import Users, User_type
from migrate_data.data import users, user_types

db.drop_all()
db.create_all()

for user_type in user_types:
	db.session.add(User_type(**user_type))

for user in users:
	db.session.add(Users(**user))


db.session.commit()