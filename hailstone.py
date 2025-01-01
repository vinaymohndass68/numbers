'''
The Hailstone sequence, also known as the Collatz conjecture or 3n + 1 problem, is a sequence of numbers defined as follows:

Start with any positive integer n.
If n is even, divide it by 2 to get the next term.
If n is odd, multiply it by 3 and add 1 to get the next term.
Repeat the process indefinitely for each new term.
The sequence is called the Hailstone sequence because the numbers often rise and fall dramatically before eventually settling into a cycle.
'''

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
start_number = int(input("Enter the starting number: "))  # You can change this value
try:
    sequence = hailstone_sequence(start_number)
    print(f"The Hailstone sequence starting from {start_number} is:", sequence)
except ValueError as e:
    print(e)