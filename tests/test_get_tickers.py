import sys

sys.path.append("./")
from src.tickers import is_valid_ticker


def test_tickers():
    print(is_valid_ticker("VLVLY"))
    print(is_valid_ticker("ABCDEFG"))


if __name__ == "__main__":
    test_tickers()
