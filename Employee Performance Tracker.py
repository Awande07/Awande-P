#EMPLOYEE PERFORMANCE TRACKER


print("=== EMPLOYEE PERFORMANCE TRACKER ===")
print("Enter the employee and their weekly performance scores (0-100). Type 'done' when finished.")
print()

employees = []
scores = []

# Data collection with input validation
while True:
    name = input("Enter employee name (or 'done' to finish): ").strip()

    if name.lower() == 'done':
        if len(scores) == 0:
            print("Please enter at least one employee before finishing.")
            continue
        break

# Input validation for scores
    while True:
        try:
            score = float(input(f"Enter {name}'s weekly performance score (0-100): "))
            if 0 <= score <= 100:
                employees.append(name)
                scores.append(score)
                break
            else:
                print("Score must be between 0 and 100!")
        except ValueError:
            print("Please enter a valid number for the score.")

# Calculate statistics
average_score = sum(scores) / len(scores)
highest_scores = max(scores)
lowest_scores = min(scores)

# Find employees for highest and lowest scores
highest_score = employees[scores.index(highest_scores)]
lowest_score = employees[scores.index(lowest_scores)]

  
# Categorize employees by performance
categories = {
    "Excellent": [],
    "Good": [],
    "Average": [],
    "Poor": [],
}

for name, score in zip(employees, scores):
    if score >= 90:
        categories["Excellent"].append(name)
    elif score >= 70:
        categories["Good"].append(name)
    elif score >= 50:
        categories["Average"].append(name)
    else:
        categories["Poor"].append(name)

# Performance report
print("\n" + "="*50)
print("EMPLOYEE PERFORMANCE REPORT")
print("="*50)

print(f"\nEmployees Statistics:")
print(f"Total Employees: {len(employees)}")
print(f"Average Score: {average_score:.2f}")
print(f"Highest Score: {highest_scores:.2f}")
print(f"Lowest Score: {lowest_scores:.2f}") 

# Table of performance categories
print("\nPerformance Category Summary:")
print("-" * 35)
print(f"{'Category':<12} {'Count':<6} {'Percentage' :<10}")
for cat in ["Excellent", "Good", "Average", "Poor"]:
    count = len(categories[cat])
    percentage = (count / len(employees)) * 100
    print(f"{cat:<12} {count:<6} {percentage:>6.1f}%")

# Employees needing improvement (performance = Poor)
print("\nEmployees Needing Improvement (Score < 50):")
print("-" * 45)
for name, score in zip(employees, scores):
    if score < 50:
        print(f"- {name} ({score:.1f})")


print("\n" + "="*50)
print("EMPLOYEE PERFORMANCE TRACKER COMPLETED! THANK YOU!")
