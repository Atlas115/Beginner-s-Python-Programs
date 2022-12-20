import random

while True: 
    user_action = input("Enter a choice (rock, paper, scissors): ")

    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)

    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"\nBoth players selected {user_action}. It's a tie!\n")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("\nRock smashes scissors! You win!\n")
        else:
            print("\nPaper covers rock! You lose.\n")
    elif user_action == "paper":
        if computer_action == "rock":
            print("\nPaper covers rock! You win!\n")
        else:
            print("\nScissors cuts paper! You lose.\n")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("\nScissors cuts paper! You win!\n")
        else:
            print("\nRock smashes scissors! You lose.\n")
    
    play_again = input("\nPlay again? (y/n): \n")
    
    if play_again.lower() != "y":
       
       break