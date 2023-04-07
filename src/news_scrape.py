from datetime import datetime

import requests
from bs4 import BeautifulSoup


def scrape_article_content(url):
    try:
        response = requests.get(url)
        if not response.ok:
            # print('Status code:', response.status_code)
            return None
        soup = BeautifulSoup(response.text, "html.parser")
        # Extract the text from the paragraphs
        paragraphs = soup.find_all("p")
        article_text = " ".join([paragraph.text for paragraph in paragraphs])
    except:
        return None
    return article_text
