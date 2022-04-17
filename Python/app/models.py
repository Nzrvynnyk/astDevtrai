from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class UserModel(db.Model):
    __tablename__ = "usertable"

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(20))
    lastname = db.Column(db.String(20))
    email = db.Column(db.String(50))
    number = db.Column(db.Integer())

    def __init__(self, firstname, lastname, email, number):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.number = number

    def __repr__(self):
        return f"{self.firstname} {self.lastname}"
