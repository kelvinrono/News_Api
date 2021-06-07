import urllib.request, json
from .models import Articles

api_key = None
base_url = None

def configure_request(app):
    global api_key, base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']


def get_news(category):
    get_news_url = base_url.format(category, api_key)
    
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        
        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)
           

    return news_results
    

def process_results(news_list):
    news_results = []
    for news_item in news_list:
        title = news_item.get('title')
        publishedAt = news_item.get('publishedAt')
        description = news_item.get('description')
        urlToImage = news_item.get('urlToImage')
        url = news_item.get('url')
        if urlToImage:

            news_object = Articles(urlToImage, description,publishedAt, title,url )
            news_results.append(news_object)

    return news_results

# def get_source(category):
#     get_news_url = base_url.format(category, api_key)
    
#     with urllib.request.urlopen(get_news_url) as url:
#         get_news_data = url.read()
#         get_news_response = json.loads(get_news_data)
        
#         source_results = None

#         if get_news_response['articles.source']:
           
#             news_source_list =  get_news_response['articles.source']
#             source_results =process_source(news_source_list) 

#     return source_results


# def process_source(source_list):
#     source_results = []
#     for source in source_list:
#         id = source.get('id')
#         name= source.get('source')

#         if id:

#             news_sources = Source(id, name,)
#             source_results.append(news_sources)

#     return source_results

