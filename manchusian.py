# Munchausen numbers are formed when the sum of all the digits in the number are raised to the power of itself is equal to itself
def munchausen_number(n):
    """Check if a number is a Münchhausen number."""
    digits = [int(digit) for digit in str(n)]
    total = sum(d ** d if d != 0 else 0 for d in digits)
    return total == n

def find_munchausen_numbers(limit):
    """Find all Münchhausen numbers up to a certain limit."""
    munchausen_numbers = []
    for num in range(limit + 1):
        if munchausen_number(num):
            munchausen_numbers.append(num)
    return munchausen_numbers

# Specify the limit
upper_limit = int(input("Enter the highest limit: ")) # You can adjust this value
munchausen_numbers = find_munchausen_numbers(upper_limit)

print(f"Münchhausen numbers up to {upper_limit} are: {munchausen_numbers}")