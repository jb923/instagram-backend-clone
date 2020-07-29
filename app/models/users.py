from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import func
from sqlalchemy.orm import validates


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    hashed_password = db.Column(db.String(128), nullable=False)
    profile_imgurl = db.Column(db.String(300))
    bio = db.Column(db.String(2000))

    post = db.relationship("Post", back_populates="user")
    comment = db.relationship("Comment", back_populates="user")
    follow = db.relationship("Follow", back_populates="user")
    like = db.relationship("Like", back_populates="user")

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "username": self.username,
            "email": self.email,
            "profileimgurl": self.profile_imgurl,
            "bio": self.bio,
        }
