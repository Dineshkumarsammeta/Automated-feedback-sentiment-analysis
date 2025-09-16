from textblob import TextBlob

def analyze_text(text: str):
    """Run sentiment analysis on a single text string."""
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity   # -1 (negative) to +1 (positive)
    subjectivity = blob.sentiment.subjectivity  # 0 (objective) to 1 (subjective)

    sentiment = (
        "positive" if polarity > 0.1 else
        "negative" if polarity < -0.1 else
        "neutral"
    )

    return {
        "text": text,
        "sentiment": sentiment,
        "polarity": round(polarity, 3),
        "subjectivity": round(subjectivity, 3)
    }
