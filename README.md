# 🎓 Student Performance ML Automation Pipeline

An end-to-end, event-driven Machine Learning pipeline designed for asynchronous batch evaluation and real-time inference using Scikit-Learn, Streamlit, and Python.

---

## 🏗️ Architecture Overview

- **`1_train_pipeline.py`**: Builds an automated Scikit-Learn Pipeline (`SimpleImputer` -> `StandardScaler` -> `RandomForestClassifier`) and serializes the trained artifact as `student_model.pkl`.
- **`2_create_data.py`**: Simulates production raw feeds with synthetic batch records containing realistic noise and missing values.
- **`3_auto_predict.py`**: Standalone batch inference module integrated with persistent logging.
- **`4_summary_report.py`**: Operational reporting engine aggregating key business metrics (Pass/Fail rates, topper analytics).
- **`run_all.py`**: Master pipeline orchestrator executing all stages sequentially.
- **`logger_setup.py`**: Configures centralized enterprise file logging (`pipeline.log`).
- **`watcher.py`**: Event-driven folder monitor. Automatically detects CSVs dropped into `inbox/`, executes predictions, logs metrics, and moves outputs/raw files to `processed/`.
- **`app.py`**: Interactive Streamlit dashboard supporting real-time parameter tuning and batch CSV drag-and-drop analytics.

---

## 🚀 Quickstart

### 1. Run Complete Batch Pipeline
```bash
python run_all.py

### 2. Start Event-Driven Folder Watcher
```bash
python watcher.py
# Drop any student CSV into the inbox/ directory to trigger automatic processing.

### 3. Launch Web Dashboard
```bash
streamlit run app.py
