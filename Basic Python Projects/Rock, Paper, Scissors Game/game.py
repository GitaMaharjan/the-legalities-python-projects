# 5.  Rock, Paper, Scissors Game   
#    *Description*: Create a game where the user plays Rock, Paper, Scissors against the computer.  
#    *Skills*: Conditionals, user input, random module.

import random

def get_computer_choice():
    options = ["rock", "paper", "scissors"]
    return random.choice(options)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a draw!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    print("Rock, Paper, Scissors Game!")
    
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Please select rock, paper, or scissors.")    
        return
    computer_choice = get_computer_choice()
    print(f"Computer: {computer_choice}")
    
    result = determine_winner(user_choice, computer_choice)
    print(result)


play_game()
