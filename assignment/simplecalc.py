"""
This program allows the user to choose an arithmetic operation to perform
on two predefined numbers. Based on the user's choice, the program calculates and displays the result with a descriptive message.
"""

# Define two variables
num1 = 10
num2 = 5

# Ask the user to choose an operation
operation = input("Which arithmetic operation would you like to perform? (sum, difference, product, quotient): ")

# Perform the chosen operation using conditional statements
if operation.lower() == 'sum':
    result = num1 + num2
    print("This is the sum of the two numbers:", result)
elif operation.lower() == 'difference':
    result = num1 - num2
    print("This is the difference of the two numbers:", result)
elif operation.lower() == 'product':
    result = num1 * num2
    print("This is the product of the two numbers:", result)
elif operation.lower() == 'quotient':
    result = num1 / num2
    print("This is the quotient of the two numbers:", result)
else:
    print("Invalid operation selected. Please choose one of +, -, *, /.")
