# # 20.  Expense Tracker   
# #     *Description*: Create a command-line application to track daily expenses.  
# #     *Skills*: File handling, lists, conditionals.

import os
from datetime import datetime

EXPENSE_FILE = 'Expense Tracker/expenses.txt'

def load_expenses():
    expenses = []
    try:
        if os.path.exists(EXPENSE_FILE):
            with open(EXPENSE_FILE, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line:  # Ensure line is not empty
                        parts = line.split(",")
                        expense = {
                            "id": int(parts[0]),
                            "date": parts[1],
                            "category": parts[2],
                            "amount": float(parts[3])
                        }
                        expenses.append(expense)
        return expenses
    except Exception as e:
        print(f"Error: Unable to load expenses. {e}")
        return []

def save_expenses(expenses):
    try:
        with open(EXPENSE_FILE, 'w') as f:
            for expense in expenses:
                line = f'{expense["id"]},{expense["date"]},{expense["category"]},{expense["amount"]}\n'
                f.write(line)
    except Exception as e:
        print(f"Error: Failed to save expenses. {e}")

def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def add_expense(expenses):
    try:
        # Validate date input
        while True:
            date = input("Enter date (YYYY-MM-DD): ")
            if is_valid_date(date):
                break
            else:
                print("Error: Invalid date. Please enter the date in the format YYYY-MM-DD.")
        
        category = input("Enter category: ")
        
        # Validate numeric amount
        while True:
            try:
                amount = float(input("Enter amount: "))
                break
            except ValueError:
                print("Error: Invalid amount. Please enter a numeric value.")
        
        expense = {
            "id": len(expenses) + 1,
            "date": date,
            "category": category,
            "amount": amount
        }
        expenses.append(expense)
        save_expenses(expenses)
        print("Expense added successfully!")
    except Exception as e:
        print(f"Error: Something went wrong while adding the expense. {e}")

def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
    else:
        for expense in expenses:
            print(f"{expense['id']}: {expense['date']} - {expense['category']} - ${expense['amount']}")

def search_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
        return
    
    while True:
        search_date = input("Enter the date to search up to (YYYY-MM-DD): ")
        if is_valid_date(search_date):
            break
        else:
            print("Error: Invalid date. Please enter the date in the format YYYY-MM-DD.")
    
    search_date_obj = datetime.strptime(search_date, '%Y-%m-%d')
    
    filtered_expenses = [expense for expense in expenses if datetime.strptime(expense['date'], '%Y-%m-%d') <= search_date_obj]
    
    if filtered_expenses:
        total_expense = 0
        print(f"Expenses up to {search_date}:")
        for expense in filtered_expenses:
            print(f"{expense['id']}: {expense['date']} - {expense['category']} - ${expense['amount']}")
            total_expense += expense['amount']
        print(f"Total expenses up to {search_date}: ${total_expense:.2f}")
    else:
        print(f"No expenses recorded up to {search_date}.")

def main():
    expenses = load_expenses()
    
    while True:
        print("\n1. Add Expense\n2. View Expenses\n3. Search Expenses by Date\n4. Exit")
        choice = input("Choose an option: ")

        try:
            if choice == '1':
                add_expense(expenses)
            elif choice == '2':
                view_expenses(expenses)
            elif choice == '3':
                search_expenses(expenses)
            elif choice == '4':
                print("Exiting the application. Goodbye!")
                break
            else:
                print("Invalid choice. Please select 1, 2, 3, or 4.")
        except Exception as e:
            print(f"Unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
