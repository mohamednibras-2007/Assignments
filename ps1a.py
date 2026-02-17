# PART A: House Hunting
# Part A: Calculates number of months required to save
# enough for a down payment based on salary and savings rate.

def calculate_months_to_save(annual_salary, portion_saved, total_cost):
    """
    Calculates the number of months required to save for a down payment.
    Returns the number of months.
    """
    current_savings = 0.0
    annual_return = 0.04
    down_payment = total_cost * 0.25
    monthly_salary = annual_salary / 12
    months = 0
    
    while current_savings < down_payment:
        # Add investment return
        current_savings += current_savings * annual_return / 12
        
        # Add monthly savings
        current_savings += monthly_salary * portion_saved
        
        # One month completed
        months += 1
    
    return months
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

months_needed = calculate_months_to_save(annual_salary, portion_saved, total_cost)
print(f"Number of months: {months_needed}")

