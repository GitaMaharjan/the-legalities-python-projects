# 23.  Random Quote Generator   
#     *Description*: Store a list of quotes in a file, and develop a program that displays a random quote each time it's run.  
#     *Skills*: File handling, random module.

import random

class QuoteGenerator:
    def __init__(self, file_path):
        self.file_path = file_path  # Store the path to the quotes file
        self.quotes = self.load_quotes()  # Load quotes from the file

    def load_quotes(self):
        try:
            with open(self.file_path, 'r') as file:  # Open the file in read mode
                quotes = file.readlines()  # Read all lines from the file
            # Strip whitespace and return only non-empty quotes
            return [quote.strip() for quote in quotes if quote.strip()]  
        except FileNotFoundError:
            return None  # Return None if the file is not found

    def get_random_quote(self):
        if not self.quotes:
            return None  # Return None if there are no quotes available
        return random.choice(self.quotes)  # Return a random quote from the list

# Example usage:
if __name__ == "__main__":  
    generator = QuoteGenerator("Random Quote Generator/quotes.txt")  # Create an instance of QuoteGenerator with the file path
    
    if generator.quotes is None:
        print(f"Error: The file '{generator.file_path}' was not found.")  # Print error if file is not found
    elif not generator.quotes:
        print("The file exists but there are no quotes available in the file.")  # Print message if file is empty
    else:
        print("Your random quote is:")  # Indicate that a random quote will be printed
        print(generator.get_random_quote())  # Print a random quote
