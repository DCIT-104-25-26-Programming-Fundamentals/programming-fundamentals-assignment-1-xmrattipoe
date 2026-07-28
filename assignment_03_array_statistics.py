def calculate_sum(numbers):
    """Return the sum of all numbers in the list, without using sum()."""
    total = 0
    for num in numbers:
        total += num
    return total
 
 
def calculate_average(numbers):
    """Return the average of the numbers in the list."""
    total = calculate_sum(numbers)
    return total / len(numbers)
 
 
def find_maximum(numbers):
    """Return the largest number in the list, without using max()."""
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest
 
 
def find_minimum(numbers):
    """Return the smallest number in the list, without using min()."""
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest
 
 
def get_numbers(count):
    """Prompt the user to enter 'count' numbers and return them as a list."""
    numbers = []
    for i in range(count):
        value = float(input(f"Enter number {i + 1}: "))
        numbers.append(value)
    return numbers
 
 
def main():
    n = int(input("How many numbers? "))
 
    if n <= 0:
        print("Error: The number of values must be a positive integer.")
        return
 
    numbers = get_numbers(n)
 
    total = calculate_sum(numbers)
    average = calculate_average(numbers)
    maximum = find_maximum(numbers)
    minimum = find_minimum(numbers)
 
    print("\nResults:")
    print(f"Sum:     {total:g}")
    print(f"Average: {average:g}")
    print(f"Maximum: {maximum:g}")
    print(f"Minimum: {minimum:g}")
 
 
if __name__ == "__main__":
    main()