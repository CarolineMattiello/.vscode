#Welcome message
print("Welcome to my Python program!")

# Prompt until we get a valid number
user_input = input("How much were your sales this week? ")
sales = float(user_input)

# Calculate monthly sales based on weekly sales
monthly_sales = sales * 4.345
print(f"You are on track to make ${monthly_sales:.2f} this month")

# Basic error handling
try:
    sales = float(sales)
except ValueError:
        print("Please enter a valid number (e.g. 1234.56).")
        exit()
