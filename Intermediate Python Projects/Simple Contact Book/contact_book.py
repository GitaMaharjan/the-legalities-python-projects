# Simple Contact Book   
#     *Description*: Build a command-line contact book where users can add, remove, and search contacts.  
#     *Skills*: Lists, file handling, conditionals.

import re

def validate_phone(number):
    # Check if the number is exactly 10 digits long and contains only digits
    return bool(re.match(r'^\d{10}$', number))

def validate_email(email):
    # Simple email validation
    return bool(re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email))

def add_contact(books):
    name = input("Enter the name of the person: \n")
    
    while True:
        number = input("Enter the number of the person (10 digits): \n")
        if validate_phone(number):
            break
        else:
            print("Invalid phone number. Please enter exactly 10 digits.")
    
    while True:
        email = input("Enter the Email of the person: \n")
        if validate_email(email):
            break
        else:
            print("Invalid email address. Please enter a valid email.")

    person_data = {"Name": name, "Number": number, "Email": email}
    books.append(person_data)
    print(f"'{person_data['Name']}' contact has been added to your book.")


def delete_contacts(books):
    if books:
        for index, book in enumerate(books, 1):
            print(f'{index}. Contacts of {book["Name"]}')
            print(f'\t Number: {book["Number"]}')
            print(f'\t Email:  {book["Email"]}')
        
        try:
            contact_index = int(input("Enter the contact index you want to delete: "))
            if 1 <= contact_index <= len(books):
                deleted_contact = books.pop(contact_index - 1)
                print(f'The contact of {deleted_contact["Name"]} is deleted successfully')
            else:
                print("Invalid contact index. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    else:
        print("Your contact book is empty")

def save_to_file(books):
    with open("contacts.txt", 'w') as file:
        for index, book in enumerate(books, 1):
            file.write(f'Contact {index}\n')
            file.write(f'Name: {book["Name"]}\n')
            file.write(f'Number: {book["Number"]}\n')
            file.write(f'Email: {book["Email"]}\n')
            file.write('\n')
    print("Contacts have been saved to the file.")
    
def search_contacts(books):
    if books:
        search_term = input("Enter name, number, or email to search for: ").lower()
        found = False
        for book in books:
            if (search_term in book["Name"].lower() or 
                search_term in book["Number"].lower() or 
                search_term in book["Email"].lower()):
                print(f'Found contact:')
                print(f'Name: {book["Name"]}')
                print(f'Number: {book["Number"]}')
                print(f'Email: {book["Email"]}')
                print('---')
                found = True
        if not found:
            print("No matching contacts found.")
    else:
        print("Your contact book is empty")
def main():
    contact_book = []
    
    while True:
        print("\nContact Book")
        print("1. Add a contact")
        print("2. Display all contacts")
        print("3. Delete a contact")
        print("4. Save the contacts")
        print("5. Search for contacts")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice of action: "))
            
            if choice == 1:
                add_contact(contact_book)
            elif choice == 2:
                display_all_contacts(contact_book)
            elif choice == 3:
                delete_contacts(contact_book)
            elif choice == 4:
                save_to_file(contact_book)
            elif choice == 5:
                search_contacts(contact_book)   
            elif choice == 6:
                save_to_file(contact_book)
                print("Exiting the contact book. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        
if __name__ == "__main__":
    main()
