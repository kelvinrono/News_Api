from ..requests import get_news
from . import main
from flask import render_template, request
from ..models import Articles

@main.route('/')
def index():
    tesla_news = get_news('tesla')
    bitcoin_news=get_news('bitcoin')
    apple_news=get_news('apple')
    title = 'Welcome to the news platform'
    return render_template('index.html', bitcoin=bitcoin_news, tesla=tesla_news, apple=apple_news)