while True:
    age = int(input("Enter your age: "))
    if age > 18:
        print("Access granted. You're an adult!")
        break
    else:
        print("Sorry, you're not old enough. Try again.")
