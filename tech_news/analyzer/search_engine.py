from tech_news.database import search_news


# Requisito 7
def search_by_title(title: str):
    response = search_news({'title': {"$regex": f'{title}', "$options": "i"}})
    return [(item['title'], item['url']) for item in response]


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
