from flask import  render_template,redirect,request,url_for,abort,flash
from . import main
from app.models import BlogPost
from ..requests import get_quotes

@main.route('/')
def index():
    '''
    This is the home page view.
    '''
    myquote = get_quotes()
    quote = myquote['quote']
    quote_author = myquote['author']

    page = request.args.get('page', 1, type=int)
    blog_posts = BlogPost.query.order_by(BlogPost.date.desc()).paginate(page=page, per_page=10)
    return render_template('index.html',blog_posts=blog_posts,quote = quote,quote_author = quote_author)