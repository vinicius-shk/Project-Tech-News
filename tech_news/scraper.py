from time import sleep
import requests
from parsel import Selector


# Requisito 1
def fetch(url):
    sleep(1)
    try:
        hearders = {"user-agent": "Fake user-agent"}
        response = requests.get(url, hearders=hearders, timeout=3)
        if response.status_code != 200:
            return None
        return response.text
    except requests.exceptions.Timeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(html_content)
    url_list = list()
    news_list = selector.css(
        "div.post-outer a.cs-overlay-link::attr(href)"
        ).getall()
    for link in news_list:
        url_list.append(link)
    return url_list


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
