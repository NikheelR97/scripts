def get_number_input(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_operation_input():
    operations = ['+', '-', '*', '/']
    while True:
        operation = input("Enter operation (+, -, *, /): ")
        if operation in operations:
            return operation
        else:
            print("Invalid operation. Please enter a valid operation.")

def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            print("Error: Cannot divide by zero.")
            return None

def main():
    print("Simple Calculator")
    print("------------------")

    num1 = get_number_input("Enter the first number: ")
    num2 = get_number_input("Enter the second number: ")
    operation = get_operation_input()

    result = calculate(num1, num2, operation)

    if result is not None:
        print(f"Result: {num1} {operation} {num2} = {result}")

    # Ask if the user wants to perform another calculation
    another_calc = input("Do you want to perform another calculation? (yes/no): ")
    if another_calc.lower() == "yes":
        main()


if __name__ == "__main__":
    main()
