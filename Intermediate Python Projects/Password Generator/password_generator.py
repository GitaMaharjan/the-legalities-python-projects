# 11.  Password Generator   
#     *Description*: Create a program that generates a random, secure password.  
#     *Skills*: String manipulation, random module, loops.

import random
import string

def password_generator(length=12):
    uppercase = string.ascii_uppercase  
    lowercase = string.ascii_lowercase  
    digits = string.digits              
    symbols = string.punctuation 

    password_chars = [
        random.choice(uppercase),  
        random.choice(lowercase),  
        random.choice(digits),     
        random.choice(symbols)     
    ]

    remaining_length = length - len(password_chars)

    all_chars = uppercase + lowercase + digits + symbols

    for _ in range(remaining_length):
        password_chars.append(random.choice(all_chars)) 

    random.shuffle(password_chars)  
    password = ''.join(password_chars)  

    print(f"The password is: {password}")

password_generator(12)
