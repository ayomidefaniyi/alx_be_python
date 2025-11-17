montly_income = int(input("Enter your montly income "))
montlu_expenses = int(input("Enter your total montly expenses "))
montly_savings = montly_income - montly_expenses
print("Your monthly savings are", montly_savings, ".")
montly_project = montly_savings * 12 + (montly_savings * 12 * 0.05)
print("Projected savings after one year, with interest, is: ", montly_project,".")
