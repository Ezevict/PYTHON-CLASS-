def password_checker():
    print("Welcome to the Secure Access System")

    # Ask the user for a password
    password = input("Please enter your password: ")

    # Check if the password matches
    if password == "MR FRANK":
        print("Access Given. Welcome!")
    else:
        print("Access Denied. Incorrect password.")

password_checker()
