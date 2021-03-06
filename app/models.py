class Source:
    """Source class to define News Source Objects"""

    def __init__(self,id,name,description,url,category,country):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.country = country

class Article:
    """Source class to define Article Objects from a news source"""

    def __init__(self,author,article_title,article_description,article_url,image_url,published):
        self.author = author
        self.article_title = article_title
        self.article_description = article_description
        self.article_url = article_url
        self.image_url = image_url
        self.published = published
        
