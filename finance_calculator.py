# Code for Finance Calculator

# First define your variables
income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your monthly expenses: "))
investment = float(input("Enter your monthly investment: "))

# Write out the calculations
savings = income - expenses - investment
savings_rate = (savings/income)*100

# Write out the conditions that govern the savings rate
# Instead of telling Python to print the result immediately, we're going to tell it to store the result in a variable called assessment.
if savings_rate >= 20:
    assessment = "Strong savings rate"
elif savings_rate >= 10:
    assessment = "Moderate savings rate"
else:
    assessment = "Needs improvement"

# Write the output statements
print(f"Savings:GHS{savings:,.2f}")
print(f"Savings rate:{savings_rate:.2f}%")
print(f"Assessment:{assessment}")

