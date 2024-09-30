# Define function for addition
def add(x, y):
    return x + y

# Define function for subtraction
def subtract(x, y):
    return x - y

# Define function for multiplication
def multiply(x, y):
    return x * y

# Define function for division with zero check
def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed"
    else:
        return x / y

# Function to display the menu and get user's choice
def get_operation_choice():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    return input("Enter choice (1/2/3/4): ")

# Function to get two numbers from the user
def get_numbers():
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    return x, y

# Main calculator function
def calculator():
    while True:
        choice = get_operation_choice()

        # Check if the choice is one of the options
        if choice in ['1', '2', '3', '4']:
            num1, num2 = get_numbers()

            if choice == '1':
                print(f"The result of addition: {add(num1, num2)}")
            elif choice == '2':
                print(f"The result of subtraction: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"The result of multiplication: {multiply(num1, num2)}")
            elif choice == '4':
                print(f"The result of division: {divide(num1, num2)}")
        else:
            print("Invalid input. Please select a valid operation.")
        
        # Check if the user wants to perform another calculation
        next_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
        if next_calculation != 'yes':
            print("Exiting the calculator. Goodbye!")
            break

# Run the calculator
calculator()
