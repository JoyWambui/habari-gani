class Config:
    """
    General configuration parent class
    """
    NEWS_BASE_URL = "https://newsapi.org/v2/top-headlines/sources?apiKey={}"



class ProdConfig(Config):
    """Production  configuration child class"""


class DevConfig(Config):
    """Development  configuration child class"""

    DEBUG = True