import sys

sys.path.append("./")
from src.financial_data import get_financial_data
from src.openai_summary import summarize_financial_data


def test_openai():
    ticker = "MSFT"
    data, news, stock_data = get_financial_data(ticker)
    summary = summarize_financial_data(news, ticker)
    print(summary)


if __name__ == "__main__":
    test_openai()
