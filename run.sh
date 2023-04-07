docker run \
  --env-file=api-keys.env \
  -p 8501:8501 \
  -d \
  --restart unless-stopped \
  stock-summary-app:latest