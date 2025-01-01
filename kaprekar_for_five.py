def kaprekar_routine_5_digit(n):
    """Perform the Kaprekar routine for five-digit numbers."""
    steps = [n]

    while True:
        # Convert number to string and zero-pad to 5 digits if needed
        str_n = str(n).zfill(5)
        
        # Create largest and smallest numbers from digits
        largest = int(''.join(sorted(str_n, reverse=True)))
        smallest = int(''.join(sorted(str_n)))
        
        # Perform the subtraction
        n = largest - smallest
        
        # If the result has already been encountered, stop the loop
        if n in steps:
            break
        steps.append(n)

    return steps

# Input a five-digit number
input_number = int(input("Enter a five digit number:" ))  # Example input
result = kaprekar_routine_5_digit(input_number)

print(f"Kaprekar routine steps for {input_number} are: {result}")
print(f"Final stable value or loop detected at: {result[-1]}")