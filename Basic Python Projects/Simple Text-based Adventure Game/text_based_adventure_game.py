# 9.  Simple Text-based Adventure Game   
#    *Description*: Build a text-based adventure game with multiple choices and endings.  
#    *Skills*: Functions, loops, conditionals, user input.

def adventure_game():
    print("Welcome to Gita's Forest Adventure Game!!\n")
    print("This game is about finding the treasure hidden in the forest.")
    start = int(input("Do you want to start the game? [1] for Yes and [2] for No.\n"))
    
    if start == 1:
        start_game()
    elif start == 2:
        print("Goodbye!")
        exit()
    else:
        print("Invalid input. Please try again.")
        adventure_game()

def start_game():
    print("\nYour goal is to find the hidden treasure and survive the challenges.")
    
    while True:
        print("\nWhich path will you choose first?")
        print("1. Climb the mountain")
        print("2. Cross the river")
        print("3. Enter the cave")
        print("4. Exit the game")
        
        choice = int(input("Enter the number of your choice (1, 2, 3, or 4): "))
        if choice == 1:
            mountain_challenge()
        elif choice == 2:
            river_challenge()
        elif choice == 3:
            cave_challenge()
        elif choice == 4:
            print("Goodbye! Thanks for playing!")
            exit()
        else:
            print("Invalid choice, please choose 1, 2, 3, or 4.")
        
        replay = input("\nDo you want to face another challenge? (yes/no): ").lower()
        if replay != "yes":
            print("Thanks for playing! Goodbye!")
            break

def mountain_challenge():
    print("\nYou chose the mountain path.")
    print("While climbing, you encounter a fearsome mountain monster.")
    print("What will you do?")
    print("1. Fight the monster")
    print("2. Hide from the monster")
    print("3. Run back to the forest path")
    
    choice = int(input("Enter the number of your choice (1, 2, or 3): "))
    if choice == 1:
        fight_monster()
    elif choice == 2:
        hide_from_monster()
    elif choice == 3:
        start_game()
    else:
        print("Invalid choice, please try again.")
        mountain_challenge()

def fight_monster():
    print("\nYou bravely fight the monster and defeat it!")
    print("You find a hidden path behind the monster leading deeper into the forest.")
    print("This path might lead to the treasure.")
    print("1. Take the hidden path")
    print("2. Return to the forest path")
    
    choice = int(input("Enter the number of your choice (1 or 2): "))
    if choice == 1:
        print("The hidden path leads you to the treasure! Congratulations, you won the game!")
    elif choice == 2:
        start_game()
    else:
        print("Invalid choice. Returning to forest path.")
        start_game()

def hide_from_monster():
    print("\nYou try to hide, but the monster finds and eats you.")
    print("You lost. Try again.")
    adventure_game()

def river_challenge():
    print("\nYou chose the river path.")
    print("You reach the riverbank and encounter the Shark King guarding the waters.")
    print("What will you do?")
    print("1. Fight the Shark King")
    print("2. Use a flying boat to cross the river")
    print("3. Return to the forest path")
    
    choice = int(input("Enter the number of your choice (1, 2, or 3): "))
    if choice == 1:
        shark_fight()
    elif choice == 2:
        boat_escape()
    elif choice == 3:
        start_game()
    else:
        print("Invalid choice, please try again.")
        river_challenge()

def shark_fight():
    print("\nYou fight the Shark King and manage to defeat him!")
    print("Behind the Shark King's lair, you find a map leading to the treasure!")
    print("You follow the map and find the treasure hidden under a tree!")
    print("Congratulations, you won the game!")
    
def boat_escape():
    print("\nYou cleverly use the flying boat to cross the river safely.")
    print("However, there is nothing else of interest here.")
    print("You return to the forest path to explore other options.")
    start_game()

def cave_challenge():
    print("\nYou enter the dark and mysterious cave.")
    print("You see two tunnels ahead. One might lead to the treasure.")
    print("1. Explore the left tunnel")
    print("2. Explore the right tunnel")
    print("3. Return to the forest path")
    
    choice = int(input("Enter the number of your choice (1, 2, or 3): "))
    if choice == 1:
        explore_left_tunnel()
    elif choice == 2:
        explore_right_tunnel()
    elif choice == 3:
        start_game()
    else:
        print("Invalid choice, please try again.")
        cave_challenge()

def explore_left_tunnel():
    print("\nThe left tunnel leads you deeper into the cave, but it is a dead end.")
    print("You return to the cave entrance.")
    cave_challenge()

def explore_right_tunnel():
    print("\nThe right tunnel leads you to a hidden chamber where the treasure is buried!")
    print("Congratulations, you found the treasure and won the game!")

adventure_game()
