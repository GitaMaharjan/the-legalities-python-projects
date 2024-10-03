# 36.  Personal Budgeting Tool   
#     *Description*: Develop a command-line budgeting tool that categorizes expenses and generates monthly reports.  
#     *Skills*: File handling, data analysis, conditionals.


from datetime import datetime
import json


class Transaction:
    def __init__(self, amount, category, date=None):
        self.amount = amount
        self.category = category
        self.date = date or datetime.now().strftime("%Y-%m-%d")
    
    def __repr__(self):
        return f"Transaction(amount={self.amount}, category={self.category}, date={self.date})"


class Budget:
    def __init__(self, income=0):
        self.income = income
        self.expenses = []  # List to store Transaction objects
    
    def set_income(self, amount):
        if amount <= 0:
            raise ValueError("Income must be a positive number.")
        if amount < self.total_expenses():
            raise ValueError(f"Income cannot be less than current total expenses (${self.total_expenses():.2f}).")
        self.income = amount  # Update the income directly instead of adding to the existing one
    
    def add_expense(self, amount, category):
        if amount <= 0:
            raise ValueError("Expense amount must be a positive number.")
        if not category or category.strip() == "":
            raise ValueError("Category cannot be empty.")
        
        # Check if category already exists
        for expense in self.expenses:
            if expense.category == category:
                expense.amount += amount  # Add amount to existing expense
                return
        
        # If category doesn't exist, create a new Transaction
        expense = Transaction(amount, category)
        self.expenses.append(expense)
    
    def total_expenses(self):
        return sum(expense.amount for expense in self.expenses)
    
    def remaining_budget(self):
        return self.income - self.total_expenses()
    
    def expenses_by_category(self):
        categories = {}
        for expense in self.expenses:
            if expense.category not in categories:
                categories[expense.category] = 0
            categories[expense.category] += expense.amount
        return categories
    
    def generate_report(self):
        print("\n--- Monthly Budget Report ---")
        print(f"Total Income: ${self.income:.2f}")
        
        categories = self.expenses_by_category()
        total_expenses = self.total_expenses()
        
        print("\nExpenses by Category:")
        for category, total in categories.items():
            print(f"{category.capitalize()}: ${total:.2f}")
        
        print(f"\nTotal Expenses: ${total_expenses:.2f}")
        print(f"Remaining Budget: ${self.remaining_budget():.2f}")


class BudgetManager:
    def __init__(self, filename="Personal Budgeting Tool/budget_data.json"):
        self.filename = filename
        self.budget = Budget()
        self.load_data()  # Automatically load existing data on initialization
    
    def load_data(self):
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                self.budget.income = data["income"]
                for exp in data["expenses"]:
                    self.budget.add_expense(exp["amount"], exp["category"])
            print("Data loaded successfully.")
        except FileNotFoundError:
            print("No saved data found, starting with a fresh budget.")
    
    def save_data(self):
        data = {
            "income": self.budget.income,
            "expenses": [{"amount": exp.amount, "category": exp.category, "date": exp.date} for exp in self.budget.expenses]
        }
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4)  # Adding indent=4 for formatted output
        print("Data saved successfully.")

    def input_income(self):
        while True:
            try:
                income = float(input(f"Enter your updated income (current total expenses: ${self.budget.total_expenses():.2f}): "))
                if income <= 0:
                    raise ValueError("Income must be a positive number.")
                if income < self.budget.total_expenses():
                    print(f"Error: The income you entered (${income:.2f}) is less than your total expenses (${self.budget.total_expenses():.2f}).")
                    choice = input("Would you like to re-enter income (R) or view your current expenses (V)? (R/V): ").strip().upper()
                    if choice == 'V':
                        self.budget.generate_report()
                    continue
                self.budget.set_income(income)  # Call set_income to update the income
                break
            except ValueError as e:
                print(f"Error: {e}. Please try again.")
    
    def input_expense(self):
        category = input("Enter expense category (food, rent, entertainment, etc.): ").lower()
        amount = float(input(f"Enter amount for {category}: "))
        self.budget.add_expense(amount, category)
    
    def main_menu(self):
        while True:
            print("\n--- Main Menu ---")
            print("1. Add Income")
            print("2. Add Expense")
            print("3. View Report")
            print("4. Save and Exit")
            
            choice = input("Choose an option: ")
            
            if choice == '1':
                self.input_income()
            elif choice == '2':
                self.input_expense()
            elif choice == '3':
                self.budget.generate_report()
            elif choice == '4':
                self.save_data()
                print("Exiting. Goodbye!")
                break
            else:
                print("Invalid option. Try again.")


if __name__ == "__main__":
    manager = BudgetManager()
    manager.main_menu()
