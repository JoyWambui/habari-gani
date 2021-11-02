from flask import render_template
from . import main
from ..requests import get_sources,get_articles

@main.route("/")
def index():
   """ View root page function that returns the index page and its data"""
   news_sources = get_sources()
   title = "Home of all your News Needs"
   return render_template("index.html",title=title,sources=news_sources)

@main.route('/articles/<source_id>')
def articles(source_id):

    """View articles page function that returns articles from a selected source."""

    articles_list = get_articles(source_id)
    

    return render_template('articles.html',articles_list = articles_list)
