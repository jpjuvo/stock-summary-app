import pandas as pd
import yfinance as yf

from src.news_scrape import scrape_article_content


def get_financial_data(ticker, limit=12000):
    stock_data = yf.Ticker(ticker)

    hist_data = get_three_month_stock_data(stock_data)

    data = stock_data.info
    keep_keys = {
        "longName": "Name",
        "averageAnalystRating": "Analyst rating",
        "forwardPE": "Forward PE",
        "epsForward": "Forward eps",
        "fiftyTwoWeekRange": "One year range",
    }

    data = {keep_keys[k]: v for k, v in data.items() if k in list(keep_keys.keys())}

    news = stock_data.news
    news_links = [n["link"] for n in news if "link" in n]
    news_articles = [scrape_article_content(url) for url in news_links]
    news_articles = [n for n in news_articles if n is not None]
    try:
        recommendations = f"{stock_data.recommendations_summary}"
    except:
        recommendations = ""
    news_data = recommendations + "\n\n".join(news_articles)
    if len(news_data) > limit:
        news_data = news_data[:limit]

    return data, news_data, hist_data


def get_three_month_stock_data(stock_data):
    end_date = pd.Timestamp.now()
    start_date = end_date - pd.DateOffset(months=3)
    hist_data = stock_data.history(start=start_date, end=end_date)
    return hist_data
