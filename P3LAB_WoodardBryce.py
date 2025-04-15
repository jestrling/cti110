def calculate_change(amount):
    """
    Calculates the most efficient number of dollars, quarters, dimes, nickels, and pennies 
    needed to make the given amount of money.

    Args:
        amount (float): The amount of money to calculate change for.

    Returns:
        None (prints the change breakdown)
    """

    if amount <= 0:
        print("No change")
        return

   
    cents = int(amount * 100)

    
    dollars = cents // 100
    cents %= 100

    
    quarters = cents // 25
    cents %= 25

    
    dimes = cents // 10
    cents %= 10

   
    nickels = cents // 5
    cents %= 5

   
    pennies = cents

   
    if dollars > 0:
        print(f"{dollars} Dollar{'s' if dollars > 1 else ''}")
    if quarters > 0:
        print(f"{quarters} Quarter{'s' if quarters > 1 else ''}")
    if dimes > 0:
        print(f"{dimes} Dime{'s' if dimes > 1 else ''}")
    if nickels > 0:
        print(f"{nickels} Nickel{'s' if nickels > 1 else ''}")
    if pennies > 0:
        print(f"{pennies} Penn{'ies' if pennies > 1 else 'y'}")



amount = float(input("Enter the amount of money as a float: $"))


calculate_change(amount) 
