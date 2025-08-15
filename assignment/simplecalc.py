"""
This program demonstrates basic arithmetic operations using two variables.
It performs addition, subtraction, multiplication, and division,
and prints the result of each operation with a descriptive message.
"""

# Define two variables
num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))

# Perform operations
sum_result = num1 + num2
sub_result = num1 - num2
mul_result = num1 * num2
div_result = num1 / num2

# Print results with descriptive text
print("This is the sum of the two numbers:", sum_result)
print("This is the difference of the two numbers:", sub_result)
print("This is the product of the two numbers:", mul_result)
print("This is the quotient of the two numbers:", div_result)
