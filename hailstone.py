def hailstone_sequence(n):
    if n <= 0:
        raise ValueError("Input must be a positive integer.")

    sequence = [n]
    
    while n != 1:
        if n % 2 == 0:  # If n is even
            n = n // 2
        else:           # If n is odd
            n = 3 * n + 1
        sequence.append(n)
    
    return sequence

# Specify the starting number for the Hailstone sequence
start_number = 36  # You can change this value
try:
    sequence = hailstone_sequence(start_number)
    print(f"The Hailstone sequence starting from {start_number} is:", sequence)
except ValueError as e:
    print(e)