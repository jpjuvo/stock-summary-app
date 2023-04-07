import sys

sys.path.append("./")
from src.financial_data import get_financial_data


def test_yfinance():
    print(get_financial_data("MSFT"))


if __name__ == "__main__":
    test_yfinance()
