from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from . import (users, posts, comments, follows, likes)