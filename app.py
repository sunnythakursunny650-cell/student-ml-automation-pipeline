import joblib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Student Performance ML Suite", layout="wide", page_icon="🎓"
)
st.title("🎓 Student Performance ML Dashboard")

# Model Loading
try:
  model = joblib.load("student_model.pkl")
  st.success("Trained Model ('student_model.pkl') Loaded Successfully!")
except Exception as e:
  st.error("Model file nahi mili! Directory verify karein.")
  st.stop()

tab1, tab2 = st.tabs(
    ["Single Student Test", "Batch File Prediction (CSV Upload)"]
)

# TAB 1: Single Prediction
with tab1:
  st.subheader("Manual Evaluation")
  c1, c2, c3 = st.columns(3)
  with c1:
    hours = st.slider("Daily Study Hours", 1.0, 12.0, 5.0, 0.5)
  with c2:
    att = st.slider("Attendance (%)", 30.0, 100.0, 75.0, 1.0)
  with c3:
    score = st.slider("Past Test Score", 10.0, 100.0, 65.0, 1.0)

  if st.button("Evaluate Student", type="primary"):
    data = pd.DataFrame(
        [[hours, att, score]],
        columns=["study_hours", "attendance", "test_score"],
    )
    pred = model.predict(data)[0]
    prob = model.predict_proba(data)[0]

    if pred == 1:
      st.success(f"### Result: PASS 🎉 (Confidence: {prob[1]*100:.1f}%)")
    else:
      st.error(f"### Result: FAIL ⚠️ (Confidence: {prob[0]*100:.1f}%)")

# TAB 2: Batch Processing with Visuals & Download
with tab2:
  st.subheader("Batch CSV Processing")
  uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

  if uploaded_file is not None:
    batch_df = pd.read_csv(uploaded_file)

    # Predictions
    preds = model.predict(
        batch_df[["study_hours", "attendance", "test_score"]]
    )
    batch_df["Result"] = ["PASS" if p == 1 else "FAIL" for p in preds]

    pass_cnt = (batch_df["Result"] == "PASS").sum()
    fail_cnt = (batch_df["Result"] == "FAIL").sum()

    m1, m2, m3 = st.columns(3)
    m1.metric("Total Records", len(batch_df))
    m2.metric("Passed", pass_cnt)
    m3.metric("Failed", fail_cnt)

    # Charts: Donut + Distribution
    col_chart1, col_chart2 = st.columns(2)

    with col_chart1:
      fig1, ax1 = plt.subplots(figsize=(4, 3))
      ax1.pie(
          [pass_cnt, fail_cnt],
          labels=["PASS", "FAIL"],
          autopct="%1.1f%%",
          colors=["#2ecc71", "#e74c3c"],
          startangle=90,
          wedgeprops=dict(width=0.4),
      )
      ax1.set_title("Pass / Fail Ratio")
      st.pyplot(fig1)

    with col_chart2:
      fig2, ax2 = plt.subplots(figsize=(4, 3))
      colors = batch_df["Result"].map({"PASS": "#2ecc71", "FAIL": "#e74c3c"})
      ax2.scatter(
          batch_df["study_hours"],
          batch_df["test_score"],
          c=colors,
          alpha=0.4,
          s=15,
      )
      ax2.set_xlabel("Study Hours")
      ax2.set_ylabel("Test Score")
      ax2.set_title("Study Hours vs Score")
      st.pyplot(fig2)

    # Download Output File
    csv_bytes = batch_df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Download Result CSV",
        data=csv_bytes,
        file_name="student_evaluation_results.csv",
        mime="text/csv",
    )

    st.dataframe(batch_df.head(15), use_container_width=True)