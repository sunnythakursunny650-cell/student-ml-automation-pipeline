import numpy as np
import pandas as pd

print("--- 1000 Students Ka Data Generate Ho Raha Hai ---")

np.random.seed(42)
n_rows = 1000

study_hours = np.random.uniform(1, 10, n_rows)
attendance = np.random.uniform(40, 100, n_rows)
test_score = (study_hours * 5) + (attendance * 0.4) + np.random.normal(0, 5, n_rows)

# Kahi-kahi missing value (NaN) daal rahe hain testing ke liye
study_hours[np.random.rand(n_rows) < 0.05] = np.nan
attendance[np.random.rand(n_rows) < 0.05] = np.nan

df_big = pd.DataFrame({
    'study_hours': study_hours,
    'attendance': attendance,
    'test_score': test_score,
})

df_big.to_csv('new_students_1000.csv', index=False)
print("[OK] 'new_students_1000.csv' file ban gayi!\n")