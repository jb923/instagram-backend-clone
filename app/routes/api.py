from flask import Blueprint, request, jsonify
import jwt

from ..models import db
from ..models.users import User
from ..models.posts import Post
from ..models.comments import Comment
from ..models.likes import Like
from ..models.follows import Follow
from ..config import Configuration


bp = Blueprint("api", __name__, url_prefix="/api")


@bp.route("/users", methods=["POST"])
def signup_user():
    data = request.json
    check_existing = User.query.filter(User.email == data['email']).first()
    if check_existing:
        return {"error": "Entered email already exists"}, 400
    if not data["email"]:
        return {"error": "Please provide an email"}, 400
    if not data["name"]:
        return {"error": "Please provide your name"}, 400
    if not data["username"]:
        return {"error": "Please provide a username"}, 400
    if not data["password"]:
        return {"error": "Please provide a password"}, 400
    if not data["confirmPassword"]:
        return {"error": "Please confirm your password"}, 400
    if data["password"] != data["confirmPassword"]:
        return {"error": "Passwords do not match"}, 400
    user = User(name=data["name"], username=data["username"], email=data['email'], password=data['password'], profile_imgurl="", bio=data["bio"])
    db.session.add(user)
    db.session.commit()
    access_token = jwt.encode({'email': user.email}, Configuration.SECRET_KEY)
    return {'access_token': access_token.decode('UTF-8'), 'user': user.to_dict()}


@bp.route("/users/<userId>")
def get_user_name(userId):
    user = User.query.filter(User.id == int(userId)).first()
    user_name = user.name
    return {"userName": user_name}
    

@bp.route("/users/session", methods=['POST'])
def signin_user():
    data = request.json
    user = User.query.filter(User.email == data['email']).first()
    if not user:
        return {"error": "Email not found"}, 422
    if user.check_password(data['password']):
        access_token = jwt.encode(
            {'email': user.email}, Configuration.SECRET_KEY)
        return {'access_token': access_token.decode('UTF-8'), 'user': user.to_dict()}
    else:
        return {"error": "Incorrect password"}, 401


@bp.route('/profileinfo/<userId>')
def get_profile_info(userId):
    user = User.query.filter(User.id == userId).first()
    posts = Post.query.filter(Post.user_id == userId).all()
    posts_count = Post.query.filter(Post.user_id == userId).count()
    followers = Follow.query.filter(Follow.follow_user_id == userId).all()
    follows = Follow.query.filter(Follow.user_id == userId).all()
    posts.reverse()

    followersList = []
    followingList = []
    
    for follower in followers:
        followersList.append(follower.to_dict())

    for follow in follows:
        followingList.append(follow.to_dict())

    followersNum = len(followersList)
    followingNum = len(followingList)

    postList = []

    for post in posts:
        post_dict = post.to_dict()
        likesNum = Like.query.filter(Like.post_id == post_dict["id"]).count()
        commentsNum = Comment.query.filter(Comment.post_id == post_dict["id"]).count()
        post_dict["numLikes"] = likesNum
        post_dict["numComments"] = commentsNum
        postList.append(post_dict)
    return {"postsNum": post_count, "posts": postList, "followersList": followersList, "followersNum": followersNum, "followingList": followingList, "followingNum": followingNum, "user": user.to_dict()}