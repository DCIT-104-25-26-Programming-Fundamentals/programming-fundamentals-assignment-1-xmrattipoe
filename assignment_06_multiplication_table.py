def print_single_table(number):
    print(f"Multiplication Table for {number}:")
    for i in range(1, 13):
        print(f"{number} x {i:<2} = {number * i}")


def print_tables_up_to_n(n):
    for number in range(1, n + 1):
        print_single_table(number)
        print("---------------------------")


if __name__ == "__main__":
    print("--- Part A: Single Table ---")
    num = int(input("Enter a number: "))
    print_single_table(num)

    print("\n--- Part B: Tables from 1 to N ---")
    n = int(input("Enter N: "))

    if n <= 0:
        print("Error: N must be a positive integer.")
    else:
        print_tables_up_to_n(n)

