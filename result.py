def show_result(user, computer):
    print("Computer chose:", computer)

    if user == computer:
        print("Result: Draw!")
    elif (user == "stone" and computer == "scissors") or \
         (user == "paper" and computer == "stone") or \
         (user == "scissors" and computer == "paper"):
        print("Result: You Win!")
    else:
        print("Result: Computer Wins!")