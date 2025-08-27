# Payroll Calculator

A simple and efficient command-line program built in Python to calculate an employee's weekly payroll, automatically handling overtime calculations.

## Features

- **User-Friendly Input:** Prompts for employee name, hours worked, and hourly rate.
- **Automatic Overtime Calculation:** Intelligently determines regular and overtime hours. Any hours worked over 40 in a week are calculated at 1.5x the regular pay rate.
- **Clear Output:** Generates a neatly formatted pay stub detailing all earnings.

## How It Works

The program uses conditional logic (`if/else` statements) to split total hours into regular and overtime hours. It then performs the necessary calculations to display regular pay, overtime pay, and total gross pay.

## Technologies Used

- Python 3
- Basic Python Syntax: Variables, Input/Output, Type Casting, Conditional Statements, Arithmetic Operators, f-Strings

## How to Run

1.  Ensure you have Python 3 installed on your system.
2.  Clone this repository or download the `payroll_calculator.py` file.
3.  Navigate to the file's directory in your terminal or command prompt.
4.  Run the program using the command:

```bash
python payroll_calculator.py
```
5.  Follow the on-screen prompts to calculate the payroll.

## Example Usage

```
==Employee Payroll Calculator==

Enter employee's name: Maria Garcia
Enter number of hours worked in a week: 45
Enter hourly pay rate: 20

Payroll information for Maria Garcia:
Hours Worked: 45.0
Hourly Rate: R20.00
Regular Pay: R800.00
Overtime Pay: R150.00
Total Pay: R950.00
==End of Payroll Information==
Thank you for your hard work!
```