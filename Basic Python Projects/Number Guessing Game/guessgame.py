# 3.  Number Guessing Game   
#    *Description*: Build a game where the program randomly selects a number, and the user has to guess it.  
#    *Skills*: Loops, random number generation, conditionals.


import random

def number_guessing_game():
    min_boundry = 1
    max_boundry= 100
    program_random_number = random.randint(min_boundry,max_boundry)
    
    attempt = 0
    
    print("Welcome to the guessing game\n")
    while True:
        try:
            guess_number = int(input("Guess the number: "))
            attempt+=1
        except ValueError:
            return "Please enter a numerical value"
        if guess_number<min_boundry or guess_number>max_boundry:
            print("Please enter the number that lies in the boundry")
        elif guess_number<program_random_number:
            print("Try again, the number is low")
        elif guess_number>program_random_number:
            print("Try again, the number is high")
        elif guess_number==program_random_number:
            print("Congratulations! You guessed right number %d in %d attempts" %(program_random_number,attempt))

number_guessing_game()