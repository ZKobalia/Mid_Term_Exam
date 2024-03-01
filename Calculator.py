def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

def get_number_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_operation_choice():
    while True:
        choice = input("Choose Operation (+, -, *, /): ")
        if choice in ('+', '-', '*', '/'):
            return choice
        else:
            print("Invalid operation. Please choose a valid operation.")

def calculator():
    while True:
        print("Calculator")

        num1 = get_number_input("Enter first number: ")
        num2 = get_number_input("Enter second number: ")

        choice = get_operation_choice()

        if choice == '+':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '-':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '*':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '/':
            print(num1, "/", num2, "=", divide(num1, num2))

        another_calculation = input("If you want to perform another calculation print 'yes': ")
        if another_calculation.lower() != 'yes':
            print("Exiting the calculator. Goodbye!")
            break

calculator()
