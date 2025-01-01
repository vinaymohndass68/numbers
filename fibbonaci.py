def fibonacci(n):
    # Initialize the first two Fibonacci numbers
    fib_sequence = [0, 1]
    
    # Generate the Fibonacci sequence up to n numbers
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    return fib_sequence

# Specify the number of Fibonacci numbers to generate
n = int(input("Enter the limit : "))  # You can change this value
fib_numbers = fibonacci(n)

print(f"The first {n} Fibonacci numbers are:", fib_numbers)