# 15.  Hangman Game   
#     *Description*: Develop a command-line Hangman game.  
#     *Skills*: Loops, conditionals, string manipulation.


# word = "string"

def raw_word(word):
    return ["_" for _ in word]

def check_word(word):
    display_word = raw_word(word)
    guessed_letters = set()
    attempts = 6  
    word = word.lower()  
    
    while "_" in display_word and attempts > 0:
        guess_alphabet = input("Enter the alphabet you guess: ").lower()
        
        # Check for valid input
        if len(guess_alphabet) != 1 or not guess_alphabet.isalpha():
            print("Please enter a single valid alphabet.")
            continue
        
        if guess_alphabet in guessed_letters:
            print("You have already guessed that alphabet.")
            continue
        
        guessed_letters.add(guess_alphabet)
        
        if guess_alphabet in word:
            print("Good Guess!!")
            for index, letter in enumerate(word):
                if letter == guess_alphabet:
                    display_word[index] = guess_alphabet
            print(f'Current word: {"".join(display_word)}')
        else:
            attempts -= 1
            print(f"Incorrect Guess! You have {attempts} attempts left.")
        
        print("Guessed Letters:", ", ".join(guessed_letters))
    
    if "_" not in display_word:
        print("Congratulations! You've guessed the word correctly!")
    else:
        print(f"Game Over! The word was: {word}")

check_word("String")
