from ..requests import get_news
from . import main
from flask import render_template, request
from ..models import Articles

@main.route('/')
def index():
    tesla_news = get_news('tesla')
    print(tesla_news)
    title = 'Welcome to the news platform'
    return render_template('index.html', title = title, tesla= tesla_news)