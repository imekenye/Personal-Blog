from flask import Blueprint
blog_posts = Blueprint('blog_posts',__name__)
from . import views