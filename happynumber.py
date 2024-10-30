def is_happy_number(n):
    """Determine if a number is a happy number."""
    def sum_of_squares_of_digits(num):
        return sum(int(digit) ** 2 for digit in str(num))

    seen_numbers = set()

    while n != 1 and n not in seen_numbers:
        seen_numbers.add(n)
        n = sum_of_squares_of_digits(n)

    return n == 1

def find_happy_numbers(limit):
    """Find all happy numbers up to a certain limit and return the count."""
    happy_numbers = []
    for num in range(1, limit + 1):
        if is_happy_number(num):
            happy_numbers.append(num)
    return happy_numbers, len(happy_numbers)

# Input the limit
limit = 100  # You can adjust this limit
happy_numbers, count = find_happy_numbers(limit)

print(f"Happy numbers up to {limit}: {happy_numbers}")
print(f"Total count of happy numbers up to {limit}: {count}")