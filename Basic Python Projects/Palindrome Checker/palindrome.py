# 6.  Palindrome Checker   
#    *Description*: Write a program that checks whether a given string is a palindrome.  
#    *Skills*: String manipulation, conditionals.

import re
def check_palindrome(word):
    normalized_word = re.sub(r'[^a-zA-Z0-9]', '', word).lower()
    
    return normalized_word == normalized_word[::-1]

word = input("Enter a string to check if it's a palindrome: ")
if check_palindrome(word):
    print(f"'{word}' is a palindrome.")
else:
    print(f"'{word}' is not a palindrome.")
