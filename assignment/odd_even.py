def odd_or_even_game():
    print("Welcome to the Odd or Even Game!")
    
    # Ask the user for a number
    try:
        number = int(input("Please enter a whole number: "))
        
        # Check if the number is odd or even
        if number % 2 == 0:
            print(f"The number {number} is EVEN ")
        else:
            print(f"The number {number} is ODD ")
    
    except ValueError:
        print("Oops! That doesn't look like a valid number. Please enter a whole number.")

odd_or_even_game()
