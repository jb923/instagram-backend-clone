import os
import boto3
from random import randrange
from flask import Blueprint, request
from ..models import db
from ..models.users import User
from ..models.posts import Post
from botocore.exceptions import ClientError
import logging

bp = Blueprint("aws", __name__, url_prefix="/api/aws")

UPLOAD_FOLDER = "uploads"
BUCKET = "appacademy-instagram-clone"

