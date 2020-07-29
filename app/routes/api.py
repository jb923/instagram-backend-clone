from flask import Blueprint, request, jsonify
import jwt

from ..models import db, User, Like, Post, Comment, Follow
from ..config import Configuration


bp = Blueprint("api", __name__, url_prefix="/api")


@bp.route("/users", methods=["POST"])
def signup_user():
    data = request.json
    check_existing = User.query.filter(User.email == data['email']).first()
    if check_existing:
        return {"error": "Entered email already exists"}, 400
    if not data["email"]:
        return {"error": "Please provide a email"}, 400
    if not data["name"]:
        return {"error": "Please provide a your name"}, 400
    if not data["username"]:
        return {"error": "Please provide a username"}, 400
    if not data["password"]:
        return {"error": "Please provide a password"}, 400
    if not data["confirmPassword"]:
        return {"error": "Please confirm your password"}, 400
    if data["password"] != data["confirmPassword"]:
        return {"error": "Passwords do not match"}, 400
        
    user = User(name=data["name"], username=data["username"], email=data['email'], password=data['password'], profileimgurl="", bio=data["bio"])
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