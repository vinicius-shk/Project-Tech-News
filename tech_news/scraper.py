from time import sleep
import requests
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    sleep(1)
    try:
        headers = {"user-agent": "Fake user-agent"}
        response = requests.get(url, headers=headers, timeout=3)
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
    selector = Selector(html_content)
    next_page = selector.css("a.next::attr(href)").get()
    if next_page:
        return next_page
    return None


# Requisito 4
def scrape_news(html_content):
    selector = Selector(html_content)
    content_dict = dict()
    content_dict["url"] = selector.css(
        "link[rel='canonical']::attr(href)"
        ).get()
    content_dict["title"] = selector.css("h1.entry-title::text").get().strip()
    content_dict["timestamp"] = selector.css("li.meta-date::text").get()
    content_dict["writer"] = selector.css("span.author > a::text").get()
    content_dict["reading_time"] = selector.css(
        "li.meta-reading-time::text"
        ).get()
    if content_dict["reading_time"][1].isdigit():
        number_str = (
            content_dict["reading_time"][0] + content_dict["reading_time"][1]
            )
        content_dict["reading_time"] = int(number_str)
    else:
        content_dict["reading_time"] = int(content_dict["reading_time"][0])
    content_dict["summary"] = ''.join(selector.css(
        "div.entry-content > p:first-of-type *::text"
        ).getall()).strip()
    content_dict["category"] = selector.css("span.label::text").get()
    return content_dict


# Requisito 5
def get_tech_news(amount):
    news_posted = list()
    next_page_url = 'https://blog.betrybe.com/'
    while len(news_posted) < amount:
        if next_page_url is None:
            break
        html_content = fetch(next_page_url)
        url_list = scrape_updates(html_content)
        next_page_url = scrape_next_page_link(html_content)
        for url in url_list:
            news_posted.append(scrape_news(fetch(url)))
    create_news(news_posted[:amount:1])
    return news_posted[:amount:1]
