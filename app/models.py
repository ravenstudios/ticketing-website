from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'




class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    department = db.Column(db.String(100), nullable=False)
    problem = db.Column(db.Text, nullable=False)
    photo_filename = db.Column(db.String(120), nullable=True)  # Store filename only
