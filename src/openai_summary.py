import os

import openai
import requests

# OpenAI API key
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
openai.api_key = OPENAI_API_KEY


def summarize_financial_data(news, ticker):
    prompt = f'News of {ticker}: "{news}"\nIs {ticker} a buy at the moment? Here\'s the summary:\n'
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    summary_news = response.choices[0].text.strip()
    return summary_news
