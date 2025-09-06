import os
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")  # headless mode for CI
import matplotlib.pyplot as plt
import seaborn as sns
import re
from textblob import TextBlob


# Step 0: Create mock CSV for CI

csv_path = "patient_feedback.csv"
if not os.path.exists(csv_path):
    df_mock = pd.DataFrame({
        "patient_id": [1, 2, 3, 4, 5],
        "feedback": [
            "Good service and friendly staff.",
            "Waited too long for my appointment.",
            "Excellent care, very satisfied.",
            "Average experience, nothing special.",
            "Poor communication from staff."
        ]
    })
    df_mock.to_csv(csv_path, index=False)


# Step 1: Load CSV

df = pd.read_csv(csv_path)


# Step 2: Data understanding

df["feedback_length"] = df["feedback"].apply(lambda x: len(str(x)))

# Save plot
os.makedirs("plots", exist_ok=True)
plt.figure()
sns.histplot(df["feedback_length"], bins=10, kde=True)
plt.title("Feedback Length Distribution")
plt.savefig("plots/feedback_length_distribution.png")
plt.close()


# Step 3: Clean data and sentiment

def clean_text(text):
    if pd.isnull(text):
        return ""
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

df["clean_feedback"] = df["feedback"].apply(clean_text)
df["sentiment_polarity"] = df["clean_feedback"].apply(lambda x: TextBlob(x).sentiment.polarity)
df["sentiment_label"] = df["sentiment_polarity"].apply(
    lambda x: "Positive" if x > 0 else ("Negative" if x < 0 else "Neutral")
)

# Sentiment plot
plt.figure()
sns.countplot(x="sentiment_label", data=df)
plt.title("Sentiment Distribution")
plt.savefig("plots/sentiment_distribution.png")
plt.close()


# Step 4: Save clean data

df_anonymized = df.drop(columns=["patient_id"])
df_anonymized.to_csv("prepared_feedback.csv", index=False)


# Step 5: CI Assertions
assert os.path.exists("prepared_feedback.csv"), "Clean CSV not generated!"
assert os.path.exists("plots/feedback_length_distribution.png"), "Feedback plot not generated!"
assert os.path.exists("plots/sentiment_distribution.png"), "Sentiment plot not generated!"
print("✅ CI checks passed: all outputs generated successfully!")
