# Tip Calculator
print("Welcome to the tip calculator!")

# Create variable to store the value of the total bill amount entered by the user
while True:
    try:
        bill = float(input("What was the total bill?: "))
    except:
        print("Whoops! That's is not a valid number. Please try again")
    else:
        break

# Create variable to store the value entered by user as a percentage for the tip
while True:
    try:
        tip_percentage = int(input("What percentage tip would you like to give?: ")) / 100
    except:
        print("Whoops! That's is not a valid number. Please try again.")
        continue
    else:
        break

# Create variable to store the value of the amount of people to split bill
while True:
    try:
        party = int(input("How many people to split the bill?: "))
    except:
        print("Whoops! That's is not a valid number. Please try again. ")
    else:
        break

# Calculate the tip using above variables and round the final answer to 2 decimals then store in result variable
result = round(bill / party + bill / party * tip_percentage, 2)
# Print the amount that each person should pay
print(f"Each person should pay: ${result}")
