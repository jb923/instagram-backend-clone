from . import db


class Follow(db.Model):
    __tablename__ = 'follows'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    follow_user_id = db.Column(db.Integer, nullable=False)

    user = db.relationship("User", back_populates="follow")

    def to_dict(self):
        return {
            "id": self.id,
            "userId": self.user_id,
            "followUserId": self.follow_user_id,
        }