def user_choice():
    options = ["stone", "paper", "scissors"]

    while True:
        user = input("Enter stone/paper/scissors: ").lower()

        if user in options:
            return user
        else:
            print("Invalid choice! Try again.")