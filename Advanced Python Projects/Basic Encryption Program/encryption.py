# 38.  Basic Encryption Program   
#     *Description*: Develop a program that encrypts and decrypts text using simple encryption algorithms like Caesar cipher.  
#     *Skills*: String manipulation, algorithms, file handling.


# Caesar Cipher Algorithm

def caesar_cipher(text, shift, direction):
    result = ""

    # Loop through each character in the text
    for char in text:
        # Check if character is an uppercase letter
        if char.isupper():
            # Shift the letter, wrapping around the alphabet
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Check if character is a lowercase letter
        elif char.islower():
            # Shift the letter, wrapping around the alphabet
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # If it's not a letter, leave it as is
            result += char

    return result

# Encrypt and Decrypt functions
def encrypt(text, shift):
    return caesar_cipher(text, shift, "encrypt")

def decrypt(text, shift):
    return caesar_cipher(text, -shift, "decrypt")

# File handling functions
def save_to_file(filename, text):
    with open(filename, 'w') as file:
        file.write(text)

def read_from_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print("File not found!")
        return None

# Main function
def main():
    print("Welcome to the Basic Encryption Program")
    
    while True:
        # Ask user if they want to encrypt or decrypt
        action = input("Would you like to (E)ncrypt or (D)ecrypt a message? (Q to quit): ").upper()

        if action == 'Q':
            print("Goodbye!")
            break

        if action not in ['E', 'D']:
            print("Invalid choice, please select 'E', 'D', or 'Q'")
            continue

        # Ask for the text
        text = input("Enter the text: ")

        # Ask for the shift value
        shift = int(input("Enter the shift key (number): "))

        # Perform the action
        if action == 'E':
            result = encrypt(text, shift)
            print(f"Encrypted text: {result}")
        else:
            result = decrypt(text, shift)
            print(f"Decrypted text: {result}")

        # Ask if they want to save the result to a file
        save = input("Would you like to save the result to a file? (Y/N): ").upper()
        if save == 'Y':
            filename = input("Enter the filename: ")
            save_to_file("Basic Encryption Program/"+filename, result)
            print(f"Result saved to {filename}")

if __name__ == "__main__":
    main()
