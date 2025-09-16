# Run all project tasks easily
.PHONY: install dev test run docker-build docker-run web

install:
\tpip install .[pipeline]

dev:
\tpip install .[dev,pipeline]

test:
\tpytest -q

# Run Flask using env variables (from .env)
run:
\tflask run --host=0.0.0.0 --port=5000

# Run the app directly (bypassing flask CLI)
web:
\tpython -m src.sentiment_pipeline.api

docker-build:
\tdocker build -t sentiment-pipeline .

docker-run:
\tdocker run --env-file .env -p 5000:5000 sentiment-pipeline
