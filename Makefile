# Run all project tasks easily
.PHONY: install dev test run docker-build docker-run

install:
\tpip install .[pipeline]

dev:
\tpip install .[dev,pipeline]

test:
\tpytest -q

run:
\tflask run --host=0.0.0.0 --port=5000

docker-build:
\tdocker build -t sentiment-pipeline .

docker-run:
\tdocker run --env-file .env -p 5000:5000 sentiment-pipeline

web:
\tpython -m src.sentiment_pipeline.api

make web

curl -X POST http://localhost:5000/analyze \
  -H "Content-Type: application/json" \
  -d '{"text": "The doctors were helpful but the waiting time was long."}'

