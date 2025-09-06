import os

# Check if mock CSV exists
assert os.path.exists("patient_feedback.csv"), "Mock CSV not found!"

# Run the main script
exit_code = os.system("python feedback_analysis_ci.py")  # replace with your script name
assert exit_code == 0, "Script failed to run!"

# Check if output files were created
assert os.path.exists("prepared_feedback.csv"), "Clean CSV not generated!"
assert os.path.exists("feedback_length_distribution.png"), "Feedback plot not generated!"
assert os.path.exists("sentiment_distribution.png"), "Sentiment plot not generated!"

print("✅ All CI checks passed successfully!")
