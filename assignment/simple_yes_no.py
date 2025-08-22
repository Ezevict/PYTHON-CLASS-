""""
Simple yes or no
"""

#Keep asking the user if he wants to continue
while True:
    answer = input("Do you want to continue? (y/n): ").lower()
    if answer == 'y':
        print("Continuing the program...")
    elif answer == 'n':
        print("Program ended.")
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
