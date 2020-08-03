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


@bp.route("/posts", methods=["POST"])
def create_post():
    data = request.json
    try:
        post = Post(user_id=data["userId"], postimgurl=data["postimgurl"], description=data["description"])
        db.session.add(post)
        db.session.commit()
        return jsonify({"post": "post created"})
    except AssertionError as message:
        print(str(message))
        return jsonify({"error": str(message)}), 400


@bp.route("/posts")
def get_all_posts():
    posts = Post.query.all()
    postsList = [post.to_dict() for post in posts]
    return {"posts": postsList}


@bp.route("/posts/<int:userId>")
def get_user_post(userId):
    try:
        fetched_posts = Post.query.filter(Post.user_id == userId).all()
        posts = [post.to_dict() for post in fetched_posts]
        return jsonify({"posts": posts})
    except AssertionError as message:
        print(str(message))
        return jsonify({"error": str(message)}), 400


@bp.route("/<int:userId>")
def get_home_feed(userId):
    postList = []

    follows = Follow.query.filter(Follow.user_id == userId).all()
    for follow in follows:
        posts = Post.query.filter((Post.user_id == follow.follow_user_id) | (Post.user_id == userId)).all()

        active_users = {}
        for post in posts:
            post_dict = post.to_dict()
            if post.user_id in active_users:
                post_dict["user_info"] = active_users[post.user_id]
            else:
                user = post.user
                active_users[post.user_id] = {"username": user.username, "profileimgurl": user.profileimgurl}
                post_dict["user_info"] = active_users[post.user_id]

            likes = Like.query.filter(Like.post_id == post.id).all()
            post_dict["LikesNum"] = len(likes)
            likesList = []
            for like in likes:
                likesList.append(like.user.to_dict())
            post_dict["likesList"] = likesList

            comments = post.comment
            commentsList = []
            for comment in comments:
                comment_dict = comment.to_dict()
                comment_likes = Like.query.filter(Like.comment_id == comment.id).all()
                userList = []
                for like in comment_likes:
                    username = like.user.to_dict()
                    userList.append(username)

                comment_dict["commentLikes"] = userList

                if comment.user_id in active_users:
                    comment_dict["username"] = active_users[comment.user_id]
                else:
                    user = comment.user
                    active_users[user.id] = {"username": user.username, "profileimgurl": user.profileimgurl}
                    comment_dict["username"] = active_users[comment.user_id]

                commentsList.append(comment_dict)
                
            post_dict["comments"] = {"commentsList": commentsList}

            postList.append(post_dict)
    return {"postList": postList}



@bp.route("/comments", methods=["POST"])
def create_comment():
    data.request.json
    try:
        comment = Comment(user_id=data["userId"], post_id=data["postId"], user_name=data["userName"], content=data["content"])
        db.session.add(comment)
        db.session.commit()
        return jsonify({"comment": "comment added"})
    except AssertionError as message:
        print(str(message))
        return jsonify({"error": str(message)}), 400


@bp.route("/comment/<int:postId>")
def get_comment(postId):
    try:
        fetched_comments = Comment.query.filter(Comment.post_id == postId).all()
        comments = [comment.to_dict() for comment in fetched_comments]
        return jsonify({"comments": comments})
    except AssertionError as message:
        print(str(message))
        return jsonify({"error": str(message)}), 400


@bp.route("/likes", methods=["POST"])
def create_like():
    data = request.json
    try:
        like = Like(
            user_id=data["userId"], post_id=data["postId"], comment_id=data["commentId"])
        db.session.add(like)
        db.session.commit()
        return jsonify({"like": "liked"})
    except AssertionError as message:
        print(str(message))
        return jsonify({"error": str(message)}), 400


@bp.route("/likes/<int:postId>")
def get_post_like(postId):
    try:
        fetched_likes = Like.query.filter(Like.post_id == postId).all()
        likes = [like.to_dict() for like in fetched_likes]
        return jsonify({"postLikes": likes})
    except AssertionError as message:
        print(str(message))
        return jsonify({"error": str(message)}), 400


@bp.route("/likes/<int:commentId>")
def get_comment_like(commentId):
    try:
        fetched_likes = Like.query.filter(Like.comment_id == commentId).all()
        likes = [like.to_dict() for like in fetched_likes]
        return jsonify({"commentLikes": likes})
    except AssertionError as message:
        print(str(message))
        return jsonify({"error": str(message)}), 400


@bp.route("/follows", methods=["POST"])
def create_follow():
    data = request.json
    check_following = Follow.query.filter(Follow.user_id == data['userId']).filter(Follow.follow_user_id == data['followUserId']).first()
    if check_following:
        return {"error": "Already following"}, 400
    try:
        follow = Follow(user_id=data["userId"],
                        follow_user_id=data["followUserId"])
        db.session.add(follow)
        db.session.commit()
        return jsonify({"follow": "following"})
    except AssertionError as message:
        print(str(message))
        return jsonify({"error": str(message)}), 400


@bp.route("/follows/<int:userId>")
def get_follow(userId):
    try:
        fetched_follows = Follow.query.filter(Follow.user_id == userId).all()
        follows = [follow.to_dict() for follow in fetched_follows]
        return jsonify({"follows": follows})
    except AssertionError as message:
        print(str(message))
        return jsonify({"error": str(message)}), 400