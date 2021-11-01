class Article:
    """Source class to define Article Objects from a news source"""

    def __init__(self,author,article_title,article_description,article_url,image_url,published):
        self.author = author
        self.title = article_title
        self.description = article_description
        self.url = article_url
        self.image_url = image_url
        self.published = published