# Part B: Saving with a Raise

# Part B: Extends Part A by including a semi-annual raise
# applied every 6 months.


annual_salary = float(input("Enter your starting annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

current_savings = 0.0
annual_return = 0.04
down_payment = total_cost * 0.25
months = 0

monthly_salary = annual_salary / 12

while current_savings < down_payment:
    # Add monthly investment return
    current_savings += current_savings * annual_return / 12
    
    # Add monthly savings
    current_savings += monthly_salary * portion_saved
    
    # One month completed
    months += 1
    
    # Apply raise after every 6 full months
    if months % 6 == 0:
        annual_salary *= (1 + semi_annual_raise)
        monthly_salary = annual_salary / 12

print(f"Number of months: {months}")
