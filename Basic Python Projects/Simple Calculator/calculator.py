# 2.  Simple Calculator   
#    *Description*: Create a basic calculator that can add, subtract, multiply, and divide two numbers.  
#    *Skills*: Functions, user input, conditionals.

def add_number(number1, number2):
    return number1+number2

def substract_number(number1,number2):
    return number1-number2

def multiply_number(number1,number2):
    return number1*number2

def divide_number(number1,number2):
    return number1 / number2

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    operation = int(input("Enter the choice of operation: "))
    
    if operation in range(1,5):
        try:
            number1=float(input("Enter the first number: "))
            number2=float(input("Enter the second number: "))
        except ValueError:
            print("Invalid Value. The input should be number")
            
        if operation==1:
            print(f"The sum of {number1} and {number2} is {add_number(number1,number2)}")
        elif operation ==2:
            print(f"The difference of {number1} and {number2} is {substract_number(number1,number2)}")
        elif operation ==3:
            print(f"The multiplication of {number1} and {number2} is {multiply_number(number1,number2)}")
        elif operation == 4:
            try:
                print(f"The division of {number1} and {number2} is {divide_number(number1,number2)}")
            except ZeroDivisionError:
                print("Cannot divide by zero")             
    else:
        print("Invalid choice. Please choose the correct operation")



calculator()