from tech_news.database import find_news


# Requisito 10
def top_5_categories():
    response = find_news()
    cat_counter = dict()
    for news in response:
        if news['category'] not in cat_counter:
            cat_counter[news['category']] = 1
        cat_counter[news['category']] += 1
    sorted_counter = sorted(
        cat_counter.items(), key=lambda x: (-x[1], x[0])
        )
    return [key for key, value in sorted_counter]
