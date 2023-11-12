import random
import sys
user_score = 0
computer_score = 0

print(f"Welcome to rock, paper, scissors!")
turn_count = 0
while True:
    turn_count += 1
    user = input("Enter your choice: ")
    user = user.lower()
    possible_actions = ["rock", "paper", "scissors"]
    computer = random.choice(possible_actions)
    if user == computer:
        print(f"Both players selected {user}. It's a tie!")
    elif user == "rock":
        if computer == "scissors":
            print("Rock smashes scissors! You win!")
            user_score += 1
        else:
            print("Paper covers rock! You lose.")
            computer_score += 1
    elif user == "paper":
        if computer == "rock":
            print("Paper covers rock! You win!")
            user_score += 1
        else:
            print("Scissors cuts paper! You lose.")
            computer_score += 1
    elif user == "scissors":
        if computer == "paper":
            print("Scissors cuts paper! You win!")
            user_score += 1
        else:
            print("Rock smashes scissors! You lose.")
            computer_score += 1
    else:
        print("Invalid input! You have not entered rock, paper or scissors, try again.")
    print(f"Player score: {user_score}")
    print(f"Computer score: {computer_score}")
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        print("Final Scores:")
        print(f"Player score: {user_score}")
        print(f"Computer score: {computer_score}")
        print(f"Total turns: {turn_count}")
        sys.exit()
