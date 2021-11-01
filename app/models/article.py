class Article:
    """Source class to define Article Objects from a news source"""

    def __init__(self,author,title,description,url,image_url,published):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.image_url = image_url
        self.published = published