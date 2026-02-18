# Part C: Finding the Right Amount to Save
# This program uses bisection search to determine
# the best savings rate required to afford the
# down payment in 36 months.

# User input
annual_salary = float(input("Enter the starting salary: "))

# Fixed assumptions for Part C
total_cost = 1000000
down_payment = total_cost * 0.25
annual_return = 0.04
semi_annual_raise = 0.07
epsilon = 100  # Acceptable error margin

# First check if saving 100% salary is enough
current_savings = 0.0
current_salary = annual_salary
monthly_salary = current_salary / 12

# Simulate 36 months with 100% savings
for month in range(1, 37):
    current_savings += current_savings * annual_return / 12
    current_savings += monthly_salary

    # Apply semi-annual raise
    if month % 6 == 0:
        current_salary *= (1 + semi_annual_raise)
        monthly_salary = current_salary / 12

# If not possible even with 100% savings
if current_savings < down_payment:
    print("It is not possible to pay the down payment in three years.")
else:
    # Bisection search setup
    low = 0.0
    high = 1.0
    steps = 0

    # Perform binary search
    while True:
        portion_saved = (low + high) / 2
        current_savings = 0.0
        current_salary = annual_salary
        monthly_salary = current_salary / 12

        # Simulate 36 months for current savings rate
        for month in range(1, 37):
            current_savings += current_savings * annual_return / 12
            current_savings += monthly_salary * portion_saved

            # Apply semi-annual raise
            if month % 6 == 0:
                current_salary *= (1 + semi_annual_raise)
                monthly_salary = current_salary / 12

        steps += 1

        # Check if within acceptable range
        if abs(current_savings - down_payment) <= epsilon:
            break
        elif current_savings < down_payment:
            low = portion_saved
        else:
            high = portion_saved

    # Output results
    print("Best savings rate:", round(portion_saved, 4))
    print("Steps in bisection search:", steps)