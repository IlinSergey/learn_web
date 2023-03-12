from datetime import datetime

import requests
from bs4 import BeautifulSoup

from webapp.model import News, db


def get_html(url: str) -> str:
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except (requests.RequestException, ValueError):
        return False


def get_python_news() -> None:
    html = get_html("https://www.python.org/blogs/")
    if html:
        soup = BeautifulSoup(html, "html.parser")
        all_news = soup.find("ul", class_="list-recent-posts").findAll("li")
        for news in all_news:
            title = news.find("a").text
            url = news.find("a")["href"]
            published = news.find("time").text
            print(published)
            try:
                published = datetime.strptime(published, "%b. %d, %Y")
                print(published)
            except ValueError:
                published = datetime.now()
            save_news(title, url, published)


def save_news(title: str, url: str, published: datetime) -> None:
    news_exists = News.query.filter(News.url == url).count()
    if not news_exists:
        news_news = News(title=title, url=url, published=published)
        db.session.add(news_news)
        db.session.commit()
