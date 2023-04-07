import sys

sys.path.append("./")
from src.news_scrape import scrape_article_content


def test_scrape():
    url = "https://finance.yahoo.com/m/f48ca171-10dc-3e1f-b2d5-575b26d42de9/3-stocks-that-have-the-most.html"
    res = scrape_article_content(url)
    print(res)


if __name__ == "__main__":
    test_scrape()
