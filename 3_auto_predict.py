import os
import joblib
import pandas as pd
from logger_setup import logger

input_csv = "new_students_1000.csv"
model_file = "student_model.pkl"
output_csv = "final_results_1000.csv"

logger.info("Auto Prediction pipeline triggered.")

if os.path.exists(input_csv) and os.path.exists(model_file):
    try:
        model = joblib.load(model_file)
        logger.info(f"Model successfully loaded: {model_file}")

        df = pd.read_csv(input_csv)
        logger.info(f"Loaded {len(df)} rows from {input_csv}")

        preds = model.predict(df[['study_hours', 'attendance', 'test_score']])
        df['Result'] = ["PASS" if p == 1 else "FAIL" for p in preds]

        df.to_csv(output_csv, index=False)
        logger.info(f"Predictions saved to {output_csv} | Processed: {len(df)}")
        print(f"[OK] Saare {len(df)} bacho ka result '{output_csv}' me save ho gaya!")
    except Exception as e:
        logger.error(f"Prediction failed with exception: {str(e)}")
        print(f"[ERROR] Process fail ho gaya: {e}")
else:
    logger.warning("Required files (CSV or Model) not found.")
    print("[ERROR] Input CSV ya model file missing hai.")