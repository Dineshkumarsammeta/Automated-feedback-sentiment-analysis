# Makefile for Automated Feedback Sentiment Analysis

# Default Python environment
PYTHON ?= python3

.PHONY: install dev test web docker-build docker-run

install:
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install .[pipeline]

dev:
	$(PYTHON) -m pip install -e .[dev,pipeline]

test:
	pytest

web:
	$(PYTHON) -m flask --app src.app run --reload

docker-build:
	docker build -t feedback-sentiment .

docker-run:
	docker run -p 5000:5000 feedback-sentiment
