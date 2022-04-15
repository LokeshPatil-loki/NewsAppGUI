from newsapi import NewsApiClient

from NewsModel import NewsModel

def getNews():
    newsapi = NewsApiClient(api_key='a4c15ce9f82a4a5898474d4c31f6d396')
    top_headlines = newsapi.get_top_headlines(country='in')["articles"]

    news_data = list()
    for x in top_headlines:
        source_name = x["source"]["name"]
        author = x["author"]
        title = x["title"]
        description = x["description"]
        url = x["url"]
        urlToImage = x["urlToImage"]
        publishedAt = x["publishedAt"]
        content = x["content"]
        news_data.append(NewsModel(source_name,author,title,description,url,urlToImage,publishedAt,content))

    return news_data
