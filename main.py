from user import user_choice
from computer import computer_choice
from result import show_result

while True:
    print("\n--- GAME MENU ---")
    print("1. Play Game")
    print("2. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        user = user_choice()
        computer = computer_choice()
        show_result(user, computer)

    elif choice == '2':
        print("Thank you!")
        break
    else:
        print("Invalid choice!")


