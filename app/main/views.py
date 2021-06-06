from ..requests import get_news
from . import main
from flask import render_template, request
from ..models import Articles

@main.route('/')
def index():
  
    title = 'Welcome to the news platform'
    return render_template('index.html', title=title)

@main.route('/bitcoin')
def bitcoin():
       bitcoin_news=get_news('bitcoin')
       return render_template('bitcoin.html', bitcoin=bitcoin_news)


@main.route('/apple')
def apple():
       apple_news=get_news('apple')
       return render_template('apple.html', apple=apple_news)


@main.route('/tesla')
def tesla():
       tesla_news=get_news('tesla')
       return render_template('tesla.html', tesla=tesla_news)
