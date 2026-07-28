def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return None
    return round(a / b, 2)


def modulus(a, b):
    if b == 0:
        return None
    return a % b


def exponent(a, b):
    return a ** b


def show_menu():
    print("============================")
    print("     SIMPLE CALCULATOR")
    print("============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")


if __name__ == "__main__":
    operations = {
        "1": ("+", add),
        "2": ("-", subtract),
        "3": ("*", multiply),
        "4": ("/", divide),
        "5": ("%", modulus),
        "6": ("**", exponent),
    }

    while True:
        show_menu()
        choice = input("Select an operation (1-7): ")

        if choice == "7":
            print("Goodbye!")
            break
        elif choice in operations:
            symbol, func = operations[choice]
            num1 = float(input("Enter first number : "))
            num2 = float(input("Enter second number: "))

            if choice in ("4", "5") and num2 == 0:
                print("Error: Cannot divide by zero.")
            else:
                result = func(num1, num2)
                print(f"Result: {num1} {symbol} {num2} = {result}")
        else:
            print("Error: Invalid choice. Please enter 1-7.")

