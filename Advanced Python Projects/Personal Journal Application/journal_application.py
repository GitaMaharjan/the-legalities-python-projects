# 32.  Personal Journal Application   
#     *Description*: Develop a command-line journal application where users can write and store daily entries.  
#     *Skills*: File handling, date and time manipulation, data organization.

import json
import os
import datetime

# Journal file to store entries
JOURNAL_FILE = "journal_entries.json"

def load_entries():
    """Load journal entries from a JSON file.
    
    Returns:
        dict: A dictionary containing journal entries categorized by type.
    """
    if os.path.exists(JOURNAL_FILE):  # Check if the journal file exists
        with open(JOURNAL_FILE, 'r') as file:  # Open the file in read mode
            return json.load(file)  # Load and return the JSON data as a dictionary
    return {}  # Return an empty dictionary if the file doesn't exist

def save_entries(entries):
    """Save journal entries to a JSON file.
    
    Args:
        entries (dict): A dictionary containing journal entries categorized by type.
    """
    with open(JOURNAL_FILE, 'w') as file:  # Open the file in write mode
        json.dump(entries, file, indent=4)  # Write the dictionary to the file in JSON format with indentation

def write_entry(entries):
    """Write a new journal entry.
    
    Args:
        entries (dict): A dictionary containing journal entries categorized by type.
    """
    category = input("Enter the category for this entry: ")  # Prompt user for entry category
    entry = input("Write your journal entry: ")  # Prompt user for the journal entry
    timestamp = datetime.datetime.now().isoformat()  # Get the current date and time in ISO format
    
    if category not in entries:  # Check if the category exists in the entries
        entries[category] = []  # If not, create a new list for that category
    
    # Append the new entry with timestamp to the corresponding category
    entries[category].append({"timestamp": timestamp, "entry": entry})
    save_entries(entries)  # Save the updated entries to the JSON file
    print("Entry saved!")  # Confirmation message

def read_entries(entries):
    """Read and display journal entries from the loaded entries.
    
    Args:
        entries (dict): A dictionary containing journal entries categorized by type.
    """
    if not entries:  # Check if there are any entries
        print("No journal entries found.")  # Notify the user if no entries exist
        return

    print("\n--- Journal Entries ---")  # Header for entries display
    for category, entries_list in entries.items():  # Iterate through each category and its entries
        print(f"\nCategory: {category}")  # Display category
        for entry in entries_list:  # Iterate through entries in the category
            print(f"{entry['timestamp']}: {entry['entry']}")  # Display timestamp and entry text
    print("-----------------------")  # Footer for entries display

def edit_entry(entries):
    """Edit an existing journal entry.
    
    Args:
        entries (dict): A dictionary containing journal entries categorized by type.
    """
    category = input("Enter the category of the entry you want to edit: ")  # Prompt for the category
    if category not in entries:  # Check if the category exists
        print(f"No entries found in category '{category}'.")  # Notify if not found
        return

    for i, entry in enumerate(entries[category]):  # Display existing entries with index
        print(f"{i + 1}. {entry['timestamp']}: {entry['entry']}")  # Show entry number, timestamp, and text

    try:
        index = int(input("Select the entry number to edit: ")) - 1  # Prompt for the entry number to edit
        if 0 <= index < len(entries[category]):  # Validate the selected index
            new_entry = input("Write the new entry: ")  # Prompt for the new entry text
            entries[category][index]['entry'] = new_entry  # Update the existing entry
            save_entries(entries)  # Save changes
            print("Entry updated!")  # Confirmation message
        else:
            print("Invalid entry number.")  # Notify if the entry number is invalid
    except ValueError:
        print("Invalid input. Please enter a number.")  # Handle non-integer input

def delete_entry(entries):
    """Delete an existing journal entry.
    
    Args:
        entries (dict): A dictionary containing journal entries categorized by type.
    """
    category = input("Enter the category of the entry you want to delete: ")  # Prompt for the category
    if category not in entries:  # Check if the category exists
        print(f"No entries found in category '{category}'.")  # Notify if not found
        return

    for i, entry in enumerate(entries[category]):  # Display existing entries with index
        print(f"{i + 1}. {entry['timestamp']}: {entry['entry']}")  # Show entry number, timestamp, and text

    try:
        index = int(input("Select the entry number to delete: ")) - 1  # Prompt for the entry number to delete
        if 0 <= index < len(entries[category]):  # Validate the selected index
            entries[category].pop(index)  # Remove the selected entry from the list
            save_entries(entries)  # Save changes
            print("Entry deleted!")  # Confirmation message
        else:
            print("Invalid entry number.")  # Notify if the entry number is invalid
    except ValueError:
        print("Invalid input. Please enter a number.")  # Handle non-integer input

def search_entries(entries):
    """Search for entries by keyword.
    
    Args:
        entries (dict): A dictionary containing journal entries categorized by type.
    """
    keyword = input("Enter a keyword to search for: ")  # Prompt for a keyword
    found = False  # Flag to track if any entry matches the keyword

    print("\n--- Search Results ---")  # Header for search results
    for category, entries_list in entries.items():  # Iterate through each category
        for entry in entries_list:  # Iterate through entries in the category
            if keyword.lower() in entry['entry'].lower():  # Check if the keyword is in the entry
                print(f"Category: {category} | {entry['timestamp']}: {entry['entry']}")  # Display matching entry
                found = True  # Set found flag to true
    if not found:  # Check if no entries were found
        print("No entries found with that keyword.")  # Notify if no matches
    print("-----------------------")  # Footer for search results

def main():
    """Main function to run the journal application."""
    entries = load_entries()  # Load existing entries from the JSON file
    
    while True:  # Main loop for the application
        print("\n--- Advanced Journal Application ---")
        print("1. Write a new entry")  # Option to write a new entry
        print("2. Read entries")  # Option to read existing entries
        print("3. Edit an entry")  # Option to edit an entry
        print("4. Delete an entry")  # Option to delete an entry
        print("5. Search entries")  # Option to search entries
        print("6. Exit")  # Option to exit the application

        choice = input("Choose an option (1-6): ")  # Prompt for user choice

        if choice == '1':
            write_entry(entries)  # Call function to write a new entry
        elif choice == '2':
            read_entries(entries)  # Call function to read entries
        elif choice == '3':
            edit_entry(entries)  # Call function to edit an entry
        elif choice == '4':
            delete_entry(entries)  # Call function to delete an entry
        elif choice == '5':
            search_entries(entries)  # Call function to search entries
        elif choice == '6':
            print("Exiting the journal application. Goodbye!")  # Exit message
            break  # Exit the main loop
        else:
            print("Invalid choice. Please try again.")  # Notify if the choice is invalid

if __name__ == "__main__":
    main()  # Run the main function when the script is executed
