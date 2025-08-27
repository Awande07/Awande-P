#Employee Payroll Calculator
print("==Employee Payroll Calculator==")
print()

#Employee Information
name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked in a week: "))
hourly_rate = float(input("Enter hourly pay rate: "))

#Employee Payroll

if hours_worked > 40:
    regular_hours = 40
    overtime_hours =hours_worked - 40
else:
    regular_hours = hours_worked
    overtime_hours = 0

#Calculate Pay
regular_pay = regular_hours * hourly_rate
overtime_pay = overtime_hours * hourly_rate * 1.5
total_pay = regular_pay + overtime_pay

#Display Payroll Information
print()
print(f"Payroll information for {name}:")
print((f"Hours Worked: {hours_worked}"))
print(f"Hourly Rate: R{hourly_rate:.2f}")
print(f"Regular Pay: R{regular_pay:.2f}")
print(f"Overtime Pay: R{overtime_pay:.2f}")
print(f"Total Pay: R{total_pay:.2f}")
print("==End of Payroll Information==")

print("Thank you for your hard work!")