import os
import subprocess
import sys
import time

# Jis folder me run_all.py hai, uska exact path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

scripts = [
    ("1. Model Training", "1_train_pipeline.py"),
    ("2. Data Generation", "2_create_data.py"),
    ("3. Auto Prediction", "3_auto_predict.py"),
    ("4. Final Report", "4_summary_report.py"),
]

print("========================================")
print("   STARTING COMPLETE ML PIPELINE        ")
print("========================================\n")

all_passed = True

for step_name, script_file in scripts:
    script_path = os.path.join(BASE_DIR, script_file)
    print(f"--> Running: {step_name} ({script_file})...")

    # Current working directory (cwd) ko ml_automation folder par set kiya
    result = subprocess.run(
        [sys.executable, script_path], cwd=BASE_DIR, capture_output=False
    )

    if result.returncode != 0:
        print(f"\n[FAIL] Error in {script_file}. Pipeline stopped.")
        all_passed = False
        break
    time.sleep(1)

if all_passed:
    print("\n========================================")
    print("   ALL TASKS COMPLETED SUCCESSFULLY!    ")
    print("========================================")