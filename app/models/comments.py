from . import db
from sqlalchemy import func


class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
    user_name = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)

    user = db.relationship("User", back_populates="comment")
    post = db.relationship("Post", back_populates="comment")
    like = db.relationship("Like", back_populates="comment")

    def to_dict(self):
        return {
            "id": self.id,
            "userId": self.user_id,
            "postId": self.post_id,
            "userName": self.user_name,
            "content": self.content,
        }
