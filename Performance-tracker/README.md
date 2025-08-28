# Employee Performance Tracker

A robust command-line application built in Python to analyze and report on employee performance metrics. This tool automates the process of calculating performance statistics, categorizing employee performance, and generating detailed reports.

## Features

- **Data Collection:** Input employee names and their weekly performance scores (0-100) with full validation.
- **Comprehensive Analysis:** Calculates average, highest, and lowest scores across the team.
- **Performance Categorization:** Automatically buckets employees into four performance categories:
  - Excellent (90-100)
  - Good (70-89)
  - Average (50-69)
  - Poor (0-49)
- **Detailed Reporting:** Generates a clean, formatted report showing:
  - Key statistics (total employees, average score, high/low scores)
  - A breakdown of employees in each performance category
  - A list of employees needing improvement (score < 50)
- **Error Handling:** Gracefully handles invalid inputs, ensuring data integrity.

## Technologies Used

- **Python 3**
- Core Python Concepts:
  - Control Flow (`if/elif/else`, `while`, `for` loops)
  - Data Structures (Lists, Dictionaries)
  - Input Validation & Error Handling (`try/except`)
  - String Formatting (f-strings)
  - Built-in Functions (`zip()`, `max()`, `min()`, `sum()`)

## How to Run

1.  Ensure you have Python 3 installed on your system.
2.  Clone this repository or download the `Employee Performance Tracker.py` file.
3.  Navigate to the file's directory in your terminal or command prompt.
4.  Run the program using the command:

```bash
python "Employee Performance Tracker.py"

## Example Usage
=== EMPLOYEE PERFORMANCE TRACKER ===

Enter employee name (or 'done' to finish): John Doe
Enter John Doe's weekly performance score (0-100): 85
Enter employee name (or 'done' to finish): Jane Smith
Enter Jane Smith's weekly performance score (0-100): 92
Enter employee name (or 'done' to finish): Bob Johnson
Enter Bob Johnson's weekly performance score (0-100): 45
Enter employee name (or 'done' to finish): done

==================================================
EMPLOYEE PERFORMANCE REPORT
==================================================

Employees Statistics:
Total Employees: 3
Average Score: 74.00
Highest Score: 92.00 (Jane Smith)
Lowest Score: 45.00 (Bob Johnson)

Performance Category Summary:
-----------------------------------
Category     Count  Percentage
Excellent    1        33.3%
Good         1        33.3%
Average      0         0.0%
Poor         1        33.3%

Employees Needing Improvement (Score < 50):
---------------------------------------------
- Bob Johnson (45.0)

==================================================
EMPLOYEE PERFORMANCE TRACKER COMPLETED! THANK YOU!