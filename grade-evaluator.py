#!/usr/bin/python3
## this is the Python application
##setting a function for the python application
import csv
import sys
import os


def load_csv_data():
    """
    Prompts the user for a filename, checks if it exists,
    and extracts all fields into a list of dictionaries.
    """
    filename = input("Enter the name of the CSV file to process (e.g., grades.csv): ")

    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)

    assignments = []

    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                assignments.append({
                    'assignment': row['assignment'],
                    'group': row['group'],
                    'score': float(row['score']),
                    'weight': float(row['weight'])
                })
        return assignments
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)


def evaluate_grades(data):
    """
    data = the list of dictionaries that load_csv_data() returned.
    Each dictionary looks like:
    {'assignment': 'Quiz', 'group': 'Formative', 'score': 85.0, 'weight': 20.0}
    """
    print("\n--- Processing Grades ---")
    if len(data) == 0:
        print("your file is empty")
        sys.exit(1)

    # a) Grade validation
    for row in data:
        if not (0 <= row['score'] <= 100):
            print(f"Attention: row of {row['assignment']} has an invalid score: {row['score']}")
            sys.exit(1)

    # b) Weight validation
    total_weight = sum(row['weight'] for row in data)
    formative_weight = sum(row['weight'] for row in data if row['group'] == 'Formative')
    summative_weight = sum(row['weight'] for row in data if row['group'] == 'Summative')

    if total_weight != 100:
        print(f"Error: total weight is {total_weight}, expected 100.")
        sys.exit(1)
    if formative_weight != 60:
        print(f"Error: Formative weight is {formative_weight}, expected 60.")
        sys.exit(1)
    if summative_weight != 40:
        print(f"Error: Summative weight is {summative_weight}, expected 40.")
        sys.exit(1)

    # c) GPA calculation
    total_grade = sum((row['score'] * row['weight'] for row in data) / 100)
    gpa = (total_grade / 100) * 5.0

    # d) Category percentages + pass/fail
    formative_score = sum(row['score'] * row['weight'] for row in data if row['group'] == 'Formative')
    formative_pct = formative_score / formative_weight

    summative_score = sum(row['score'] * row['weight'] for row in data if row['group'] == 'Summative')
    summative_pct = summative_score / summative_weight

    status = "PASSED" if formative_pct >= 50 and summative_pct >= 50 else "FAILED"
#f) print results
    print(f"Formative: {formative_pct:.2f}% Summative: {summative_pct:.2f}%")
    print(f"Total Grade: {total_grade:.2f}  GPA: {gpa:.2f}")
    print(f"Status: {status}")


    # e) Resubmission logic
    failed_formatives = [row for row in data if row['group'] == 'Formative' and row['score'] < 50]
    resubmit_list = []
    max_weight =0

    for row in failed_formative:
        if row['weight'] > max_weight:
             max_weight = row['weight']
    resubmission_list = []
    for row in failed_formative:
        if row['weight'] == max_weight:
            resubmission.append(row)

    if resubmit_list:
        print("Eligible for resubmission:", ", ".join(resubmit_list))

        for row in resubmission_list:
            print(f"-{assignment[row]}")
    else:
        print("no submission required")



if __name__ == "__main__":
    # 1. Load the data
    course_data = load_csv_data()

    # 2.Process the features
    evaluate_grades(course_data)
