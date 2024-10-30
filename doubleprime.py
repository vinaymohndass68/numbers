def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_primes_up_to(n):
    """Count the number of prime numbers from 1 to n (inclusive)."""
    count = 0
    for num in range(2, n + 1):
        if is_prime(num):
            count += 1
    return count

def double_prime_numbers(limit):
    """Find all double prime numbers up to a specified limit."""
    double_primes = []
    for n in range(2, limit + 1):
        prime_count = count_primes_up_to(n)
        if is_prime(prime_count):
            double_primes.append(n)
    
    return double_primes

# Specify the upper limit
upper_limit = 18  # You can change this value
double_primes = double_prime_numbers(upper_limit)

print(f"Double prime numbers up to {upper_limit} are:", double_primes)