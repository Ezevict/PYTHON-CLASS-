def get_directions():
    print("Welcome")
    
    # Get user's name
    name = input("Please enter your name: ")
    
    # Get destination choice
    print(f"Hi {name}, where would you like to go today?")
    print("Options: Abakpa or Emene")
    destination = input("Enter your destination: ").strip().lower()

    # Directions based on destination
    if destination == "abakpa":
        print(f"\nAlright {name}, here's how you can get to Abakpa from Aptech:")
        print("1. When you come out of Aptech, cross over to the other side of road.")
        print("2. Stop and enter Keke heading to Holy Ghost.")
        print("3. Stop at Holy Ghost Bus-stop, then walk down to the Bus park.")
        print("4. Look for Bus loading passengers going to Abakpa, then enter the Bus heading to Abakpa.")
        print("5. You’ll arrive in Abakpa in about 20–30 minutes depending on traffic.")
    elif destination == "emene":
        print(f"\nGreat choice {name}, here's how you can get to Emene from Aptech:")
        print("1. When you come out of Aptech, cross over to the other side of road.")
        print("2. Stop and enter Keke heading to Holy Ghost.")
        print("3. Stop at Holy Ghost Bus-stop, then walk down to the Bus park.")
        print("4. Look for Bus loading passengers going to Emene, then enter the Bus heading to Emene.")
        print("5. You should arrive in Emene in about 35 minutes.")
    else:
        print(f"\nSorry {name}, I can only provide directions to Abakpa or Emene.")

get_directions()
