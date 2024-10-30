def is_reverse_divisible(n, d):
    """Check if a number is reverse-divisible by a given divisor."""
    # Reverse the digits of the number
    reversed_n = int(str(n)[::-1])
    return reversed_n % d == 0

def find_reverse_divisible_numbers(limit, divisor):
    """Find all reverse-divisible numbers up to a certain limit."""
    reverse_divisible_numbers = []
    for num in range(1, limit + 1):
        if is_reverse_divisible(num, divisor):
            reverse_divisible_numbers.append(num)
    return reverse_divisible_numbers

# Specify the limit and divisor
upper_limit = 1000  # You can adjust this value
divisor = 7         # You can change the divisor as needed

reverse_divisible_numbers = find_reverse_divisible_numbers(upper_limit, divisor)
print(f"Reverse-divisible numbers up to {upper_limit} that are divisible by {divisor} are: {reverse_divisible_numbers}")