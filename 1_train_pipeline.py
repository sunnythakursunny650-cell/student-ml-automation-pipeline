import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

print("--- Training Pipeline Start ---")

# Training ke liye sample data
data = {
    'study_hours': [2, 5, np.nan, 8, 1, 7, 3, np.nan, 9, 4],
    'attendance': [60, 80, 75, 95, 40, np.nan, 65, 85, 90, 70],
    'test_score': [45, 70, 65, 90, 30, 85, 50, 78, 92, 55],
    'passed': [0, 1, 1, 1, 0, 1, 0, 1, 1, 0],
}

df = pd.DataFrame(data)
X = df[['study_hours', 'attendance', 'test_score']]
y = df['passed']

# Auto cleaning + scaling + training pipeline
pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler()),
    ('model', RandomForestClassifier(random_state=42)),
])

pipeline.fit(X, y)

# Trained pipeline ko save karna
joblib.dump(pipeline, 'student_model.pkl')
print("[OK] Model train hokar 'student_model.pkl' save ho gaya!\n")