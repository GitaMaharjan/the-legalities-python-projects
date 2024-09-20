# 19.  Basic CRUD Application   
#     *Description*: Develop a command-line CRUD (Create, Read, Update, Delete) application for managing notes.  
#     *Skills*: File handling, lists, functions.
import os

# File to store notes
NOTE_FILE = "Basic CRUD Application/notes.txt"


def read_notes():
    """Read notes from the file and return as a list."""
    if not os.path.exists(NOTE_FILE):
        return []

    try:
        with open(NOTE_FILE, 'r') as file:
            return file.read().strip().split('\n')
    except Exception as e:
        print(f"Error reading notes: {e}")
        return []


def write_notes(notes):
    """Write the notes to the file."""
    try:
        with open(NOTE_FILE, 'w') as file:
            file.write('\n'.join(notes))
    except Exception as e:
        print(f"Error writing notes: {e}")


def create_note():
    """Create a new note."""
    note = input("Enter the note: ")
    if not note.strip():
        print("Note cannot be empty.")
        return

    notes = read_notes()
    notes.append(note)
    write_notes(notes)
    print("Note added!")


def read_note():
    """Display all notes."""
    notes = read_notes()
    if notes and any(note.strip() for note in notes):
        print("Notes:")
        for index, note in enumerate(notes, start=1):
            if note.strip():  # Show only non-empty notes
                print(f"{index}. {note}")
    else:
        print("No notes available.")


def update_note():
    """Update an existing note."""
    read_note()
    try:
        index = int(input("Enter the note number to update: ")) - 1
        notes = read_notes()

        if 0 <= index < len(notes):
            new_note = input("Enter the new note: ")
            if not new_note.strip():
                print("Note cannot be empty.")
                return
            notes[index] = new_note
            write_notes(notes)
            print("Note updated!")
        else:
            print("Invalid note number.")
    except ValueError:
        print("Please enter a valid number.")
    except Exception as e:
        print(f"Error updating note: {e}")


def delete_note():
    """Delete a note."""
    read_note()
    try:
        index = int(input("Enter the note number to delete: ")) - 1
        notes = read_notes()

        if 0 <= index < len(notes):
            notes.pop(index)
            write_notes(notes)
            print("Note deleted!")
        else:
            print("Invalid note number.")
    except ValueError:
        print("Please enter a valid number.")
    except Exception as e:
        print(f"Error deleting note: {e}")


def main():
    """Main function to run the CRUD application."""
    while True:
        print("\nNote Management System")
        print("1. Create Note")
        print("2. Read Notes")
        print("3. Update Note")
        print("4. Delete Note")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            create_note()
        elif choice == '2':
            read_note()
        elif choice == '3':
            update_note()
        elif choice == '4':
            delete_note()
        elif choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
