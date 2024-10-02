# 33.  Simple Inventory Management System   
#     *Description*: Create a command-line inventory system to manage products, stock levels, and orders.  
#     *Skills*: File handling, lists, dictionaries, conditionals.
import json  # Importing json module to handle file reading/writing in JSON format
import os  # Importing os module to check if files exist

class InventoryManager:
    def __init__(self, inventory_file='inventory.json', order_file='orders.json'):
        # Constructor method, initializes inventory and order files
        self.inventory_file = inventory_file  # File to store inventory data
        self.order_file = order_file  # File to store order data
        self.load_inventory()  # Load inventory from file when class is instantiated
        self.load_orders()  # Load orders from file when class is instantiated

    def load_inventory(self):
        """Load inventory from a file or create an empty one."""
        if os.path.exists(self.inventory_file):  # Check if the inventory file exists
            with open(self.inventory_file, 'r') as file:  # Open the file in read mode
                self.inventory = json.load(file)  # Load inventory data from the file
        else:
            self.inventory = {}  # If file doesn't exist, create an empty inventory

    def save_inventory(self):
        """Save inventory to a file."""
        with open(self.inventory_file, 'w') as file:  # Open the file in write mode
            json.dump(self.inventory, file, indent=4)  # Save inventory data to the file

    def load_orders(self):
        """Load orders from a file or create an empty list."""
        if os.path.exists(self.order_file):  # Check if the order file exists
            with open(self.order_file, 'r') as file:  # Open the file in read mode
                self.orders = json.load(file)  # Load order data from the file
        else:
            self.orders = []  # If file doesn't exist, create an empty order list

    def save_orders(self):
        """Save orders to a file."""
        with open(self.order_file, 'w') as file:  # Open the file in write mode
            json.dump(self.orders, file, indent=4)  # Save order data to the file

    def add_product(self, name, quantity):
        """Add a new product or increase the quantity of an existing product."""
        if name in self.inventory:  # Check if the product already exists in inventory
            self.inventory[name]['quantity'] += quantity  # Increase the product quantity
            print(f'{quantity} units of {name} added. New stock: {self.inventory[name]["quantity"]}.')
        else:
            self.inventory[name] = {'quantity': quantity}  # Add a new product to inventory
            print(f'Added new product: {name} with {quantity} units.')
        self.save_inventory()  # Save updated inventory to file

    def delete_product(self, name):
        """Delete a product from the inventory."""
        if name in self.inventory:  # Check if the product exists in inventory
            del self.inventory[name]  # Remove the product from inventory
            print(f'Product {name} has been deleted.')
        else:
            print(f'Product {name} not found.')  # Display message if product doesn't exist
        self.save_inventory()  # Save updated inventory to file

    def edit_product(self, current_name, new_name=None, new_quantity=None):
        """Edit a product's name and/or quantity."""
        if current_name in self.inventory:  # Check if the product exists in inventory
            if new_name:  # If a new name is provided
                self.inventory[new_name] = self.inventory.pop(current_name)  # Change the product's name
                print(f'Product name updated from {current_name} to {new_name}.')
            if new_quantity is not None:  # If a new quantity is provided
                self.inventory[new_name or current_name]['quantity'] = new_quantity  # Update the product's quantity
                print(f'{new_name or current_name} quantity updated to {new_quantity}.')
            self.save_inventory()  # Save updated inventory to file
        else:
            print(f'Product {current_name} not found.')  # Display message if product doesn't exist

    def view_inventory(self):
        """Display the current inventory."""
        print("Current Inventory:")  # Print inventory title
        for name, details in self.inventory.items():  # Loop through inventory items
            print(f"- {name}: {details['quantity']} in stock")  # Display product name and stock level
        if not self.inventory:  # If inventory is empty
            print("Inventory is empty.")  # Inform the user

    def place_order(self, name, quantity):
        """Place an order for a product and reduce its stock."""
        if name in self.inventory and self.inventory[name]['quantity'] >= quantity:  # Check if enough stock exists
            self.inventory[name]['quantity'] -= quantity  # Deduct the ordered quantity from inventory
            order = {'product': name, 'quantity': quantity}  # Create an order record
            self.orders.append(order)  # Add the order to the order list
            print(f'Order placed: {quantity} units of {name}.')
            self.save_inventory()  # Save updated inventory to file
            self.save_orders()  # Save updated orders to file
        else:
            print(f'Cannot place order. Insufficient stock of {name}.')  # Display error if not enough stock

    def view_orders(self):
        """View the list of all orders and mark them as done."""
        if not self.orders:  # Check if there are any orders
            print("No orders placed yet.")  # Inform the user if no orders
            return  # Exit function if no orders

        print("Order History:")  # Print order history title
        for idx, order in enumerate(self.orders, start=1):  # Loop through all orders with index
            print(f"{idx}. {order['quantity']} units of {order['product']}")  # Display order details

        while True:  # Loop to allow user to mark orders as done
            choice = input("Enter the order number to mark as done (or 'b' to go back): ")  # Prompt user input
            if choice.lower() == 'b':  # If user chooses to go back
                break  # Exit the loop
            else:
                try:
                    order_index = int(choice) - 1  # Convert input to integer and adjust index for list (0-based)
                    if 0 <= order_index < len(self.orders):  # Check if the input is a valid order number
                        fulfilled_order = self.orders.pop(order_index)  # Remove the fulfilled order
                        print(f"Order {fulfilled_order['quantity']} units of {fulfilled_order['product']} has been fulfilled and removed.")
                        self.save_orders()  # Save updated orders to file
                        break  # Exit the loop after processing
                    else:
                        print("Invalid order number. Please try again.")  # Error message for invalid number
                except ValueError:
                    print("Invalid input. Please enter a valid number or 'b' to go back.")  # Error message for non-integer input

    def main(self):
        """Main menu to manage the inventory and orders."""
        while True:  # Infinite loop for menu system
            print("\nInventory and Order Management System")  # Print menu title
            print("1. Add Product")  # Menu option 1
            print("2. Delete Product")  # Menu option 2
            print("3. Edit Product")  # Menu option 3
            print("4. View Inventory")  # Menu option 4
            print("5. Place Order")  # Menu option 5
            print("6. View Orders")  # Menu option 6
            print("7. Exit")  # Menu option 7

            choice = input("Enter your choice: ")  # Prompt user input for menu selection

            if choice == '1':
                name = input("Enter product name: ")  # Get product name from user
                quantity = int(input("Enter quantity to add: "))  # Get quantity to add
                self.add_product(name, quantity)  # Call add_product method
            elif choice == '2':
                name = input("Enter product name to delete: ")  # Get product name to delete
                self.delete_product(name)  # Call delete_product method
            elif choice == '3':
                current_name = input("Enter current product name: ")  # Get current product name
                new_name = input("Enter new name (leave blank to keep the current name): ")  # Get new product name (optional)
                new_quantity = input("Enter new quantity (leave blank to keep current quantity): ")  # Get new product quantity (optional)
                new_quantity = int(new_quantity) if new_quantity else None  # Convert quantity to integer if provided
                self.edit_product(current_name, new_name or None, new_quantity)  # Call edit_product method
            elif choice == '4':
                self.view_inventory()  # Call view_inventory method
            elif choice == '5':
                name = input("Enter product name: ")  # Get product name for order
                quantity = int(input("Enter quantity to order: "))  # Get quantity for order
                self.place_order(name, quantity)  # Call place_order method
            elif choice == '6':
                self.view_orders()  # Call view_orders method
            elif choice == '7':
                print("Exiting...")  # Exit message
                break  # Exit the loop and end program
            else:
                print("Invalid choice. Please try again.")  # Error message for invalid menu input

# Instantiate the class and run the main menu
if __name__ == "__main__":
    manager = InventoryManager()  # Create an instance of the InventoryManager class
    manager.main()  # Call the main method to start the menu system
