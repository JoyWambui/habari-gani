import urllib.request,json
from .models import Source,Article

api_key = None
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_BASE_URL']

def get_sources():
    """Function that gets the json response to our url request"""
    get_sources_url = base_url.format(api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_results(sources_results_list)


    return sources_results

def process_results(sources_list):
    """Function that processes the sources results and transforms them to a list of Source Objects"""
    
    sources_results = []
    for single_source in sources_list:
        id = single_source.get("id")
        name = single_source.get("name")
        description = single_source.get("description")
        url = single_source.get("url")
        category = single_source.get("category")
        country = single_source.get("country")
        
        source_object = Source(id,name,description,url,category,country)
        sources_results.append(source_object)

    return sources_results

def get_articles(source_id):
    "Function that returns articles from a selected news source"
    get_articles_url = "https://newsapi.org/v2/everything?sources={}&apiKey={}".format(source_id,api_key)
    
    with urllib.request.urlopen(get_articles_url) as url:
        source_articles_data = url.read()
        source_articles_response = json.loads(source_articles_data)
        articles_results = None
        
        if source_articles_response['articles']:
            sources_results_list = source_articles_response['articles']
            articles_results = process_articles(sources_results_list)
        
        
            
        
    return articles_results

def process_articles(articles_list):
    """Function that processes the article results and transforms them to a list of Article Objects"""
    articles_results = []
    for article in articles_list:
        author = article.get("author")
        article_title = article.get("title")
        article_description = article.get("description")
        article_url = article.get("url")
        image_url = article.get("urlToImage")
        published = article.get("publishedAt") 
        
        if image_url:
            articles_object = Article(author,article_title,article_description,article_url,image_url,published)
            articles_results.append(articles_object)
    
    return articles_results
    


