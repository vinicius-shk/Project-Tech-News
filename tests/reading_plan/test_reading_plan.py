from unittest.mock import patch
import pytest
from tech_news.analyzer.reading_plan import ReadingPlanService  # noqa: F401, E261, E501

MOCK_DB = [{
  "url": "https://blog.betrybe.com/novidades/noticia-bacana",
  "title": "Notícia bacana",
  "timestamp": "04/04/2021",
  "writer": "Eu",
  "reading_time": 4,
  "summary": "Algo muito bacana aconteceu",
  "category": "Ferramentas",
}, {
  "url": "https://blog.betrybe.com/novidades/noticia-bacana",
  "title": "Notícia longa",
  "timestamp": "04/04/2021",
  "writer": "Eu",
  "reading_time": 24,
  "summary": "Algo muito bacana aconteceu",
  "category": "Ferramentas",
}, {
  "url": "https://blog.betrybe.com/novidades/noticia-bacana",
  "title": "Notícia legal",
  "timestamp": "04/04/2021",
  "writer": "Eu",
  "reading_time": 3,
  "summary": "Algo muito bacana aconteceu",
  "category": "Ferramentas",
}, {
  "url": "https://blog.betrybe.com/novidades/noticia-bacana",
  "title": "Notícia longa 2",
  "timestamp": "04/04/2021",
  "writer": "Eu",
  "reading_time": 10,
  "summary": "Algo muito bacana aconteceu",
  "category": "Ferramentas",
}]


def test_reading_plan_group_news():
    with patch('tech_news.analyzer.reading_plan.find_news') as mock_find_news:
        mock_find_news.return_value = MOCK_DB
        news_by_time = ReadingPlanService.group_news_for_available_time(10)
        print(news_by_time)
        assert len(news_by_time['readable']) == 2
        assert len(news_by_time['unreadable']) == 1
        assert news_by_time["readable"][0]['unfilled_time'] == 3
        with pytest.raises(ValueError):
            ReadingPlanService.group_news_for_available_time(0)
