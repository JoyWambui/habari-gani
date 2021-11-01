from app import app
from .models import source
Source = source.Source

api_key = app.config["NEWS_API_KEY"]
base_url = app.config["NEWS_BASE_URL"]

def get_sources():
    """Function that gets the json response to our url request"""
    get_sources_url = base_url.format(api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['results']:
            sources_results_list = get_sources_response['results']
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
