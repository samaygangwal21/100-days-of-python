print("Welcome to the tip calculator!")
bill   = float(input("What was the total bill? $"))
tip    = int(input("What percentage tip would you like to give?"))
people = int(input("How many people to split the bill? "))
print(f"Each person should pay {(bill + (tip/100 *bill))/people}")

# Output:
# Welcome to the tip calculator!
# What was the total bill? $150
# What percentage tip would you like to give?10
# How many people to split the bill? 5
# Each person should pay 33.0