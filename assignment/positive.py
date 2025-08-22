while True:
    number = int(input("Enter a positive number: "))
    if number < 0:
        print("Negative number detected. Program stopped.")
        break
    else:
        print(f"You entered: {number}")