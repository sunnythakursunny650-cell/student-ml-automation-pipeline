import os
import pandas as pd

result_file = "final_results_1000.csv"

print("--- Automated Summary Generator ---")

if os.path.exists(result_file):
    df = pd.read_csv(result_file)
    total_students = len(df)
    pass_count = (df['Result'] == 'PASS').sum()
    fail_count = (df['Result'] == 'FAIL').sum()
    pass_percentage = (pass_count / total_students) * 100

    print("\n==============================")
    print("      FINAL BATCH REPORT      ")
    print("==============================")
    print(f"Total Students Evaluated : {total_students}")
    print(f"Total Passed             : {pass_count}")
    print(f"Total Failed             : {fail_count}")
    print(f"Overall Pass Percentage  : {pass_percentage:.2f}%")
    print("==============================\n")

    best_student = df.loc[df['test_score'].idxmax()]
    print(f"Highest Score: {best_student['test_score']:.2f} (Hours: {best_student['study_hours']:.1f}, Attendance: {best_student['attendance']:.1f}%)")
else:
    print(f"[ERROR] '{result_file}' nahi mili!")