from tech_news.database import search_news
from datetime import datetime


def factory_search(news: list):
    return [(item['title'], item['url']) for item in news]


# Requisito 7
def search_by_title(title: str):
    response = search_news({'title': {"$regex": f'{title}', "$options": "i"}})
    return factory_search(response)


# Requisito 8
def search_by_date(date):
    try:
        datetime.strptime(date, '%Y-%m-%d')
        news_date = f'{date[8:]}/{date[5:7]}/{date[:4]}'
        response = search_news({'timestamp': f'{news_date}'})
        return factory_search(response)
    except ValueError:
        raise ValueError('Data inválida')


# Requisito 9
def search_by_category(category):
    response = search_news(
        {'category': {"$regex": f'{category}', "$options": "i"}}
        )
    return factory_search(response)
