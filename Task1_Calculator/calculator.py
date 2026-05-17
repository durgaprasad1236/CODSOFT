# ============================================
# Simple Calculator Project
# Author: N.Durga prasad 
# Date: 12/05/2026
# Description: A basic calculator that can
#              add, subtract, multiply, divide
# ============================================


# Function to show welcome message
def show_welcome():
    print("=" * 40)
    print("      Welcome to Simple Calculator      ")
    print("=" * 40)
    print("This calculator can do basic operations")
    print("like +, -, *, /")
    print("=" * 40)


# Function to get a number from the user
def get_number(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            # This happens when user types letters instead of numbers
            print("Oops! That's not a valid number. Please try again.")


# Function to get the operator from the user
def get_operator():
    valid_operators = ["+", "-", "*", "/"]
    while True:
        operator = input("Enter operator (+, -, *, /): ").strip()
        if operator in valid_operators:
            return operator
        else:
            print("Invalid operator! Please choose from +, -, *, /")


# Function to do the actual calculation
def calculate(num1, operator, num2):
    if operator == "+":
        result = num1 + num2

    elif operator == "-":
        result = num1 - num2

    elif operator == "*":
        result = num1 * num2

    elif operator == "/":
        # Check if user is trying to divide by zero
        if num2 == 0:
            print("Error: You cannot divide by zero!")
            return None
        result = num1 / num2

    return result


# Function to show the result nicely
def show_result(num1, operator, num2, result):
    print("\n--- Result ---")
    # Round to 4 decimal places to keep it clean
    print(f"{num1} {operator} {num2} = {round(result, 4)}")
    print("-" * 14)


# Main function where everything runs
def main():
    show_welcome()

    # Keep running until the user wants to quit
    while True:
        print()

        # Step 1: Get first number
        num1 = get_number("Enter first number: ")

        # Step 2: Get the operator
        operator = get_operator()

        # Step 3: Get second number
        num2 = get_number("Enter second number: ")

        # Step 4: Do the calculation
        result = calculate(num1, operator, num2)

        # Step 5: Show the result (only if calculation was successful)
        if result is not None:
            show_result(num1, operator, num2, result)

        # Step 6: Ask user if they want to do another calculation
        print()
        again = input("Do you want to calculate again? (yes/no): ").strip().lower()

        # Accept "yes" or "y" to continue
        if again not in ["yes", "y"]:
            print()
            print("Thanks for using the calculator. Goodbye!")
            print("=" * 40)
            break


# This is the starting point of the program
if __name__ == "__main__":
    main()