from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash


db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(20), nullable=False)
    username = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    hashed_password = db.Column(db.String(128), nullable=False)
    profileimgUrl = db.Column(db.String(200))
    bio = db.Column(db.String(2000))
    
    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)

    def to_dict(self):
        return {"id": self.id, "full_name": self.full_name, "username": self.username, "email": self.email, "profileimgUrl": self.profileimgUrl, "bio": self.bio}


class Like(db.Model):
    __tablename__ = 'likes'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    liked = db.Column(db.Boolean, nullable=False)

    user = db.relationship("User", back_populates='likes')

    def to_dict(self):
        return {"id": self.id, "user_id": self.user_id, "liked": self.liked}


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    imgUrl = db.Column(db.String(1000), nullable=False)
    description = db.Column(db.String(2000), nullable=True)

    user = db.relationship("User", back_populates="posts")
    comments = db.relationship("comment", back_populates="posts")

    def to_dict(self):
        return {"id": self.id, "user_id": self.user_id, "imgUrl": self.imgUrl, "description": self.description}


class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"), nullable=False)
    content = db.Column(db.String(2000), nullable=False)

    user = db.relationship("User", back_populates="comments")
    post = db.relationship("Post", back_populates="comments")

    def to_dict(self):
        return {"id": self.id, "user_id": self.user_id, "post_id": self.post_id, "description": self.content}
