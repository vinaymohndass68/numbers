def kaprekar_routine_495(n):
    """Perform the Kaprekar routine for three-digit numbers until reaching 495."""
    kaprekar_constant = 495
    steps = [n]

    while n != kaprekar_constant:
        # Convert number to string and zero-pad to 3 digits
        str_n = str(n).zfill(3)
        # Create largest and smallest numbers
        largest = int(''.join(sorted(str_n, reverse=True)))
        smallest = int(''.join(sorted(str_n)))
        # Perform the subtraction
        n = largest - smallest
        steps.append(n)

    return steps

# Input a three-digit number
input_number = 578  # Example input
result = kaprekar_routine_495(input_number)
print(f"Kaprekar routine steps for {input_number} to reach 495 are: {result}")