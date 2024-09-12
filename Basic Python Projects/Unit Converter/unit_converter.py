# 10.  Unit Converter (e.g., miles to kilometers)   
#     *Description*: Develop a program that converts units (e.g., miles to kilometers, Celsius to Fahrenheit).  
#     *Skills*: Functions, conditionals, user input.

def unit_converter():
    print("Welcome to the Unit Converter!")
    print("Select the conversion you want to perform:")
    print("1. Meter to Kilometer")
    print("2. Kilometer to Meter")
    print("3. Meter to Centimeter")
    print("4. Centimeter to Meter")
    print("5. Miles to Kilometers")
    print("6. Kilometers to Miles")
    print("7. Celsius to Fahrenheit")
    print("8. Fahrenheit to Celsius")
    
    choice = int(input("\nEnter the number of your choice (1-8): "))
    
    if choice == 1:
        meters = float(input("Enter value in meters: "))
        kilometers = meters / 1000
        print(f"{meters} meters is equal to {kilometers} kilometers.")
    
    elif choice == 2:
        kilometers = float(input("Enter value in kilometers: "))
        meters = kilometers * 1000
        print(f"{kilometers} kilometers is equal to {meters} meters.")
    
    elif choice == 3:
        meters = float(input("Enter value in meters: "))
        centimeters = meters * 100
        print(f"{meters} meters is equal to {centimeters} centimeters.")
    
    elif choice == 4:
        centimeters = float(input("Enter value in centimeters: "))
        meters = centimeters / 100
        print(f"{centimeters} centimeters is equal to {meters} meters.")
    
    elif choice == 5:
        miles = float(input("Enter value in miles: "))
        kilometers = miles * 1.60934
        print(f"{miles} miles is equal to {kilometers} kilometers.")
    
    elif choice == 6:
        kilometers = float(input("Enter value in kilometers: "))
        miles = kilometers / 1.60934
        print(f"{kilometers} kilometers is equal to {miles} miles.")
    
    elif choice == 7:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C is equal to {fahrenheit}°F.")
    
    elif choice == 8:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F is equal to {celsius}°C.")
    
    else:
        print("Invalid choice. Please try again.")
        unit_converter()  

unit_converter()
