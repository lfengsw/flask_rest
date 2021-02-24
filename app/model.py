from flask_restful import abort

from app.ext import db

class Letter(db.Model):
    __tablename__ = 'letters'
    id = db.Column(db.Integer,primary_key=True)
    letter = db.Column(db.String(5))
    cities = db.Column(db.String(20))

class City(db.Model):
    __tablename__ = 'cities'
    id = db.Column(db.Integer, primary_key=True)
    regionName = db.Column(db.String(20))
    cityCode = db.Column(db.Integer)
    pinYin = db.Column(db.String(20))
    letter_id = db.Column(db.Integer)

class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20),unique=True)
    password = db.Column(db.String(20))
    token = db.Column(db.String(50))
    permission = db.Column(db.Integer)

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except:
            return False
        else:
            return True


class AddressModel(db.Model):
    __tablename__='address'
    id = db.Column(db.Integer,primary_key=True)
    uid = db.Column(db.Integer)
    detail=db.Column(db.String(128))

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except:
            return False
        else:
            return True





