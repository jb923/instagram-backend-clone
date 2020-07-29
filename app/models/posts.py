from . import db
from sqlalchemy import func


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    post_imgurl = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String, nullable=False)

    user = db.relationship("User", back_populates="post")
    comment = db.relationship("Comment", back_populates="post")
    like = db.relationship("Like", back_populates="post")

    def to_dict(self):
        return {
            "id": self.id,
            "userId": self.user_id,
            "postimgurl": self.post_imgurl,
            "description": self.description,
        }