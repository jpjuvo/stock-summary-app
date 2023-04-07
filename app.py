import plotly.graph_objs as go
import streamlit as st

from src.financial_data import get_financial_data
from src.openai_summary import summarize_financial_data
from src.tickers import is_valid_ticker


def plot_stock_data(ticker, data):
    trace = go.Candlestick(
        x=data.index,
        open=data["Open"],
        high=data["High"],
        low=data["Low"],
        close=data["Close"],
        name=ticker,
    )

    layout = go.Layout(title=f"{ticker} Stock Data (3 Months)")
    fig = go.Figure(data=[trace], layout=layout)
    return fig


# Set the page title and favicon
st.set_page_config(page_title="Stock Summary App", page_icon=":chart_with_upwards_trend:")

# Add a title and description
st.title("Stock summary")
st.markdown("Enter a stock ticker and get a summary of its financial data.")

# Get user input for the stock ticker
ticker = st.text_input("Enter the stock ticker:")

# Fetch and display financial data when the user clicks the button
if st.button("Get Summary"):
    if ticker and is_valid_ticker(ticker):
        data, news, stock_data = get_financial_data(ticker)

        stock_chart = plot_stock_data(ticker, stock_data)
        st.plotly_chart(stock_chart)

        summary = summarize_financial_data(news, ticker)
        st.write("\n".join([f"- **{k}:** {v} " for k, v in data.items()]))
        st.write(f"Is {ticker} a buy?")
        st.write(summary)

    else:
        st.warning("Please enter a valid stock ticker. i.e. MSFT")
