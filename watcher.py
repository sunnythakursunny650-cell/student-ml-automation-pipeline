import os
import shutil
import time
import joblib
import pandas as pd
from logger_setup import logger

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INBOX_DIR = os.path.join(BASE_DIR, "inbox")
PROCESSED_DIR = os.path.join(BASE_DIR, "processed")
MODEL_FILE = os.path.join(BASE_DIR, "student_model.pkl")

# Folders ensure karein
os.makedirs(INBOX_DIR, exist_ok=True)
os.makedirs(PROCESSED_DIR, exist_ok=True)

print("========================================")
print("     LIVE ML FOLDER WATCHER ACTIVE      ")
print(f" Watching folder: {INBOX_DIR}")
print(" Press Ctrl + C anytime to stop.")
print("========================================\n")

# Model pehle se load karke ready rakhein
model = joblib.load(MODEL_FILE)

while True:
  # Inbox folder check karein
  files = [f for f in os.listdir(INBOX_DIR) if f.endswith(".csv")]

  for filename in files:
    input_filepath = os.path.join(INBOX_DIR, filename)
    print(f"\n[NEW FILE DETECTED] Processing: {filename}")
    logger.info(f"Watcher detected incoming file: {filename}")

    try:
      df = pd.read_csv(input_filepath)

      # Predict
      preds = model.predict(df[["study_hours", "attendance", "test_score"]])
      df["Result"] = ["PASS" if p == 1 else "FAIL" for p in preds]

      # Output processed folder me save karein
      output_filename = f"result_{filename}"
      output_filepath = os.path.join(PROCESSED_DIR, output_filename)
      df.to_csv(output_filepath, index=False)

      logger.info(
          f"Watcher finished {filename}. Saved to {output_filename} | Total:"
          f" {len(df)}"
      )
      print(f"[SUCCESS] Result saved in 'processed/{output_filename}'")

      # Raw file ko inbox se hatakar processed me archive kar do
      shutil.move(input_filepath, os.path.join(PROCESSED_DIR, f"raw_{filename}"))

    except Exception as e:
      logger.error(f"Watcher error on {filename}: {str(e)}")
      print(f"[ERROR] Process failed: {e}")

  time.sleep(2)  # Har 2 second me check karega