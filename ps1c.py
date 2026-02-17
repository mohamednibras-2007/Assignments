# Part C: Finding the Right Amount to Save (Refactored Version)

def simulate_savings(annual_salary, portion_saved):
    
    """
    Simulates savings growth over 36 months with
    semi-annual raises and annual return.
    Returns final savings amount.
    """

    total_cost = 1000000
    down_payment = total_cost * 0.25
    annual_return = 0.04
    semi_annual_raise = 0.07
    
    current_savings = 0.0
    current_salary = annual_salary
    monthly_salary = current_salary / 12
    
    for month in range(1, 37):
        # Add investment return
        current_savings += current_savings * annual_return / 12
        
        # Add monthly savings
        current_savings += monthly_salary * portion_saved
        
        # Apply raise every 6 months
        if month % 6 == 0:
            current_salary *= (1 + semi_annual_raise)
            monthly_salary = current_salary / 12
    
    return current_savings


# ---- Main Program ----

annual_salary = float(input("Enter the starting salary: "))
total_cost = 1000000
down_payment = total_cost * 0.25
epsilon = 100

# First check if saving 100% is enough
max_savings = simulate_savings(annual_salary, 1.0)

if max_savings < down_payment:
    print("It is not possible to pay the down payment in three years.")
else:
    low = 0.0
    high = 1.0
    steps = 0
    
    while True:
        portion_saved = (low + high) / 2
        current_savings = simulate_savings(annual_salary, portion_saved)
        
        steps += 1
        
        if abs(current_savings - down_payment) <= epsilon:
            break
        elif current_savings < down_payment:
            low = portion_saved
        else:
            high = portion_saved
    
    print(f"Best savings rate: {round(portion_saved, 4)}")
    print(f"Steps in bisection search: {steps}")
