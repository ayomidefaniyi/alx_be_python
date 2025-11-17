income = int(input("Enter your montly income? "))
expenses = int(input("Enter your total montly expenses "))
savings = income - expenses
print("Your monthly savings are", savings, ".")
project = savings * 12 + (savings * 12 * 0.05)
print("Projected savings after one year, with interest, is: ", project,".")
