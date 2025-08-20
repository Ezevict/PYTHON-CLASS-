def find_greater_number():
    print("🔢 Let's find out which number is greater!")

    try:
        # Get two numbers from the user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Compare the numbers
        if num1 > num2:
            print(f"The greater number is: {num1}")
        elif num2 > num1:
            print(f"The greater number is: {num2}")
        else:
            print("Both numbers are equal.")
    
    except ValueError:
        print("Please enter valid numbers only!")

# Run the program
find_greater_number()
