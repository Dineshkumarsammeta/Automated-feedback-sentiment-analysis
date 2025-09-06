import os
import pandas as pd

# Mock CSV path
csv_path = "patient_feedback.csv"

# Create mock CSV for CI if not exists
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

# Verify the file now exists
assert os.path.exists(csv_path), "Mock CSV not found!"

# Run the main script
exit_code = os.system("python feedback_analysis_ci.py")  # replace with your script name
assert exit_code == 0, "Script failed to run!"

# Check output files
assert os.path.exists("prepared_feedback.csv"), "Clean CSV not generated!"
assert os.path.exists("plots/feedback_length_distribution.png"), "Feedback plot not generated!"
assert os.path.exists("plots/sentiment_distribution.png"), "Sentiment plot not generated!"

print("✅ All CI checks passed successfully!")
