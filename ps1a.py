# PART A: House Hunting
# Part A: Calculates number of months required to save
# enough for a down payment based on salary and savings rate.


annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

current_savings = 0.0
annual_return = 0.04
down_payment = total_cost * 0.25
months = 0
monthly_salary = annual_salary / 12

while current_savings < down_payment:
    current_savings += current_savings * annual_return / 12
    current_savings += monthly_salary * portion_saved
    months += 1

print("Number of months: " + str(months))
