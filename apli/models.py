from apli import db

class Task (db.Model):
    id = db.Column (db.Integer, primary_key=True)
    content = db.Column(db.String(200))
    done = db.Column(db.Boolean)

db.create_all()