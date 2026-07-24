# Project name: Lab 1: Grade Evaluator & Organizer
this project contains two tools:
### 1. **`grade evaluator.py`**: 
   - It reads a csv of assignment grades, validates it and calculates the final GPA, decides Pass/Fail status, and reports any Formative assignments
   - check the eligibility for resubmission.
### 2. **`organizer.sh`**
   — archives the current `grades.csv`, timestamps it, resets the
   workspace with a fresh empty `grades.csv`, and logs every run.

## Requirements

- Python 3
- Bash (Linux/macOS, or WSL/Git Bash on Windows)
- A `grades.csv` file in the same directory, with the following columns:

  ```csv
  assignment                               group           score        weight
  Quiz                                     Formative         85             20
  Group Exercise                           Formative         40             20
  Functions and Debugging Lab              Formative         45             20
  Midterm Project - Simple Calculator      Summative         70             20
  Final Project - Text-Based Game          Summative         60             20
  ```

  - `group` must be either `Formative` or `Summative`.
  - `score` must be between 0 and 100.
  - `weight` values must sum to 100 overall, with Formative weights summing to
    exactly 60 and Summative weights summing to exactly 40.

## Running the code
- 1st:
 clone the repository that we are using form "Github" by accessing it in github under "code" and under "code/https"
<img width="1218" height="472" alt="image" src="https://github.com/user-attachments/assets/d4322aea-407a-432d-a48e-8f8bf373fd6d" />


- 2nd:
 you access the repo which is now a directory under the WSL terminal you are using 
**`cd the_name_of_the_repo`**  (the name of the repo in this example is: **Lab1_Daniella189-hub**
  <img width="938" height="235" alt="image" src="https://github.com/user-attachments/assets/218df6d8-191a-4483-8ab9-fc03a7ec9279" />


- 3rd:
 You need to recognize which file you would like to run:
    In our example we are using "grade-evaluator.py" and "organizer.sh"

## 1. Running the "grade-evaluator.py" file

From the project directory(**Lab1_Daniella189-hub**):

```bash
chmod +x grade-evaluator.py
```
next
```bash
python3 grade-evaluator.py
```
or 
```bash
./grade-evaluator.py
```

The script will prompt you for a filename:

```
Enter the name of the CSV file to process (e.g., grades.csv): grades.csv
```

Type the filename (e.g. `grades.csv`) and press Enter.

### What it does

- **Score validation** — confirms every score is within 0–100. If any score is out of
  range, the program reports which assignment(s) and stops.
- **Weight validation** — confirms total weight = 100, Summative weight = 40, and
  Formative weight = 60. If the split is wrong, the program reports the issue and stops.
- **GPA calculation** — computes each assignment's weighted contribution
  (`score × weight / 100`), sums them into a Total Grade out of 100, then applies
  `GPA = (Total Grade / 100) * 5.0`.
- **Pass/Fail decision** — a student passes only if their in-category percentage is
  **≥ 50% in both** the Formative group and the Summative group (not just the overall
  total).
- **Resubmission logic** — among *failed* Formative assignments (score < 50), the
  one(s) with the **highest weight** are flagged as eligible for resubmission. If
  several failed assignments tie for the highest weight, all of them are listed.

### Error handling

- If the file you name doesn't exist, the program prints an error and exits.
- If the CSV file exists but is empty (e.g. right after `organizer.sh` resets it), the
  program prints an error and exits instead of crashing.

## 2. Running the Organizer Script

Make the script executable once:

```bash
chmod +x organizer.sh
```

Then run it from the project directory whenever you want to archive the current grades
and start fresh:

```bash
./organizer.sh
```

### What it does

1. Creates an `archive/` directory if one doesn't already exist.
2. Generates a timestamp (`YYYYMMDD-HHMMSS`).
3. Renames `grades.csv` to `grades_<timestamp>.csv` and moves it into `archive/`.
4. Creates a new, empty `grades.csv` in the project directory so it's ready for the
   next batch.
5. Appends a line to `organizer.log` recording the timestamp, original filename, and
   archived filename. `organizer.log` accumulates a new entry every time the script
   is run.

### Example log entry

```
[20260724-150203] Original: grades.csv -> Archived: archive/grades_20260724-150203.csv
```

## Typical Workflow

```bash
# 1. Evaluate the current batch of grades
python3 grade-evaluator.py
# (enter: grades.csv)

# 2. Archive it and reset the workspace for the next batch
./organizer.sh

# 3. Drop a new grades.csv into the folder and repeat
```

