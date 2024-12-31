def generate_primes(limit):
    # Initialize a boolean array where True means prime
    primes = [True] * (limit + 1)
    p = 2
    
    while p * p <= limit:
        # If prime[p] is still True, it is a prime
        if primes[p]:
            # Mark all multiples of p as False (not prime)
            for i in range(p * p, limit + 1, p):
                primes[i] = False
        p += 1

    # Collecting all prime numbers
    prime_numbers = [p for p in range(2, limit + 1) if primes[p]]
    
    # Return both the prime numbers and their count
    return prime_numbers, len(prime_numbers)

# Specify the upper limit for finding prime numbers
limit =  int(input("Enter the limit required: "))  # You can change this value
prime_numbers, prime_count = generate_primes(limit)

print(f"Prime numbers up to {limit} are:", prime_numbers)
print(f"Total number of prime numbers found: {prime_count}")