# 5. Personal Finance Calculator

interest = 0.05

income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your total monthly expenses: "))

savings = income - expenses

projectedSavings = savings * 12 + (savings * 12 * interest)

print("Your monthly savings are $" , savings, sep ="")
print("Projected savings after one year, with interest, is: $", projectedSavings , sep = "")
