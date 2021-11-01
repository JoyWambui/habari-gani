class Config:
    """
    General configuration parent class
    """
    NEWS_BASE_URL = "https://newsapi.org/v2/top-headlines/sources?apiKey={}"



class ProdConfig(Config):
    """Production  configuration child class"""
    NEWS_API_KEY = "7f464afbc50c446ea2cc7c94a9bd334f"


class DevConfig(Config):
    """Development  configuration child class"""

    DEBUG = True