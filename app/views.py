from flask import render_template
from app import views
from .requests import get_sources

@app.route("/")
def index():
   """ View root page function that returns the index page and its data"""
   news_sources = get_sources()
   title = "Home of all your News Needs"
   return render_template("index.html",title=title,sources=news_sources)