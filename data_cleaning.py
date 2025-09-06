import matplotlib
matplotlib.use('Agg')  # headless backend for CI
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
from textblob import TextBlob
import os
# updated 
# Reproducibility 
np.random.seed(42)


# Mock CSV for CI Testing

mock_csv_path = "patient_feedback.csv"
if not os.path.exists(mock_csv_path):
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
    df_mock.to_csv(mock_csv_path, index=False)


# Step 1: Load Data

df = pd.read_csv(mock_csv_path)
print("🔍 Raw Data Sample")
print(df.head())


# Step 2: Data Understanding

print("\n📏 Dataset Shape:", df.shape)
print("\n🧾 Column Info:")
print(df.info())
print("\n❓ Missing Values Check:")
print(df.isnull().sum())

# Feedback length distribution
df["feedback_length"] = df["feedback"].apply(lambda x: len(str(x)))
plt.figure()
sns.histplot(df["feedback_length"], bins=10, kde=True)
plt.title("Feedback Length Distribution")
plt.savefig("feedback_length_distribution.png")
plt.close()

# Step 3: Data Cleaning

def clean_text(text):
    if pd.isnull(text):
        return ""
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

df["clean_feedback"] = df["feedback"].apply(clean_text)

# Sentiment Scoring
df["sentiment_polarity"] = df["clean_feedback"].apply(lambda x: TextBlob(x).sentiment.polarity)
df["sentiment_label"] = df["sentiment_polarity"].apply(
    lambda x: "Positive" if x > 0 else ("Negative" if x < 0 else "Neutral")
)

print("\n✅ After Cleaning & Sentiment Scoring:")
print(df[["patient_id", "feedback", "clean_feedback", "sentiment_label"]].head())


# Step 4: Data Quality Checks

duplicates = df.duplicated().sum()
print(f"🔁 Duplicate Records: {duplicates}")

plt.figure()
sns.countplot(x="sentiment_label", data=df)
plt.title("Sentiment Distribution")
plt.savefig("sentiment_distribution.png")
plt.close()


# Step 5: Anonymization

df_anonymized = df.drop(columns=["patient_id"])
print("\n🔒 Anonymized Data Preview:")
print(df_anonymized.head())

# Step 6: Save Clean Data

df_anonymized.to_csv("prepared_feedback.csv", index=False)
print("💾 Clean data exported as 'prepared_feedback.csv'")
