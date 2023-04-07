# Stock summary app

Stock summarization app that runs locally with Streamlit web UI. The app retrieves news and financial data from Yahoo finance and uses OpenAI API for news summarization.

Note that each query costs around 0.02-0.15$ in OpenAI API costs. Your mileage may vary so monitor the costs.

![app](./media/baba_stock.png)

# Install

- Requires [docker](https://docs.docker.com/get-docker/)
- create an `api-keys.env` file with `OPENAI_API_KEY=abcdxxxxx...xxx` content

```bash
sh build.sh
```

# Run

```bash
sh run.sh
```

Open the [web app](http://0.0.0.0:8501)

App keeps running until it's stopped even after reboot. To stop, use docker kill.
