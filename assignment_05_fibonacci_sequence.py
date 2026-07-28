def generate_fibonacci_terms(n):
    """Return a list containing the first n terms of the Fibonacci sequence,
    generated using a loop (not recursion)."""
    sequence = []
    a, b = 0, 1
 
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
 
    return sequence
 
 
def print_first_n_terms():
    """Part A: Ask the user for N and print the first N Fibonacci terms."""
    n = int(input("How many terms? "))
 
    if n <= 0:
        print("Error: N must be a positive integer.")
        return
 
    sequence = generate_fibonacci_terms(n)
    sequence_str = " ".join(str(term) for term in sequence)
    print(f"Fibonacci sequence: {sequence_str}")
 
 
def is_fibonacci_number(number):
    """Part B: Return True if 'number' appears in the Fibonacci sequence,
    generated using a loop (not recursion)."""
    if number < 0:
        return False
 
    a, b = 0, 1
 
    while a <= number:
        if a == number:
            return True
        a, b = b, a + b
 
    return False
 
 
def check_number():
    """Part B: Ask the user for a number and report whether it's Fibonacci."""
    number = int(input("Enter a number to check: "))
 
    if is_fibonacci_number(number):
        print(f"{number} is a Fibonacci number.")
    else:
        print(f"{number} is NOT a Fibonacci number.")
 
 
def main():
    print_first_n_terms()
    print()
    check_number()
 
 
if __name__ == "__main__":
    main()
 