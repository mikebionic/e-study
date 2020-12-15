from main import db, create_app

app = create_app()
app.app_context().push()


from migrate_data.data import users

db.drop_all()
db.create_all()

db.session.commit()
