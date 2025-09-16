FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies for NLTK/Matplotlib/wordcloud
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    python3-dev \
    libfreetype6-dev \
    libpng-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY pyproject.toml ./
COPY src ./src
COPY requirements.txt ./requirements.txt

# Install dependencies (base + pipeline extras)
RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    pip install .[pipeline]

# Copy entrypoint 
CMD ["python", "-m", "src.sentiment_pipeline.api"]

