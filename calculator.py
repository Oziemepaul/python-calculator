
# This program is a basic calculator that performs a selected operation on two numbers.

# Ask the user to input the first number
try:
    num1 = float(input("Enter the first number: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit()

# Ask the user to input the second number
try:
    num2 = float(input("Enter the second number: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit()

# Ask the user to input the mathematical operation
operation = input("Enter the mathematical operation (+, -, *, /): ")

# Perform the calculation based on the user's input
if operation == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == '/':
    # Check for division by zero
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please enter +, -, *, or /.")