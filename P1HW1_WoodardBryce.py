# Your Name: Bryce Woodard
# Date: April 4, 2025
# Assignment Name: P1LAB1
# Creating a program to calculate exponents


print("-----Calculating Exponenets----\n")


base = int(input("Enter an integer as the base value: "))
exponent = int(input("Enter an integer as the exponent: "))


result = base ** exponent
print(f"\n{base} raised to the power of {exponent} is {result} !!\n")


print("-----Addition and Subtraction----\n")


start_num = int(input("Enter a starting integer: "))
add_num = int(input("Enter an integer to add: "))
subtract_num = int(input("Enter an integer to subtract: "))


final_result = start_num + add_num - subtract_num
print(f"\n{start_num} + {add_num} - {subtract_num} is equal to {final_result}")
