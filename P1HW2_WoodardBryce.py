# Bryce Woodard
# April 4th,2025
# P1HW2 - Travel Budget
# This program asks the user to enter their budget, travel destination, and expected expenses.
# It then calculates the total expenses and remaining budget.


budget = float(input("Enter your budget: "))


destination = input("Enter your travel destination: ")


gas = float(input("Enter amount you will spend on gas: "))
accommodation = float(input("Enter amount you will spend on accommodation: "))
food = float(input("Enter amount you will spend on food: "))


total_expenses = gas + accommodation + food


remaining_budget = budget - total_expenses


print("\n------------Travel Expenses------------")
print(f"Location: {destination}")
print(f"Initial Budget: ${budget:.2f}")
print(f"\nExpenses")
print(f"Gas: ${gas:.2f}")
print(f"Accommodation: ${accommodation:.2f}")
print(f"Food: ${food:.2f}")
print("\n----------------------------------------")
print(f"Remaining Balance: ${remaining_budget:.2f}")
