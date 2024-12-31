def is_narcissistic_number(n):
    """Check if a number is a Narcissistic number."""
    num_str = str(n)
    power = len(num_str)
    total_sum = sum(int(digit) ** power for digit in num_str)
    return total_sum == n

def find_narcissistic_numbers(limit):
    """Find all Narcissistic numbers up to a certain limit."""
    narcissistic_numbers = []
    for num in range(1, limit + 1):
        if is_narcissistic_number(num):
            narcissistic_numbers.append(num)
    return narcissistic_numbers

# Input the limit
limit = int(input("Enter the limit: "))  # You can adjust this limit
narcissistic_numbers = find_narcissistic_numbers(limit)

print(f"Narcissistic numbers up to {limit}: {narcissistic_numbers}")