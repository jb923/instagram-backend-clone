from flask import Blueprint, request, jsonify
import jwt

from ..models.models import db, User, Like, Post, Comment
from ..config import Configuration


bp = Blueprint("api", __name__, url_prefix="/api")

@bp.route("/users", methods=["POST"])
def signup_user():
    print(request.json)
    data = request.json
    user = User(full_name=data["firstName"], email=data['email'], password=data['password'])
    db.session.add(user)
    db.session.commit()
    access_token = jwt.encode({'email': user.email}, Configuration.SECRET_KEY)
    return {'access_token': access_token.decode('UTF-8'), 'user': user.to_dict()}



@bp.route("/")
def get_posts():
    fetechedPosts = Post.query.all()
    posts = [post.to_dict() for post in fetechedPosts]
    return {"Posts": post}

