def kaprekar_routine(n):
    """Perform the Kaprekar routine until reaching 6174."""
    if len(str(n)) != 4 or len(set(str(n))) < 2:
        raise ValueError("Input must be a four-digit number with at least two different digits.")

    kaprekar_constant = 6174
    steps = [n]

    while n != kaprekar_constant:
        # Convert number to string and zero-pad to 4 digits
        str_n = str(n).zfill(4)
        # Create largest and smallest numbers
        largest = int(''.join(sorted(str_n, reverse=True)))
        smallest = int(''.join(sorted(str_n)))
        # Perform the subtraction
        n = largest - smallest
        steps.append(n)

    return steps

# Input a four-digit number
input_number = int(input("Input a four digit number with atleast two different digits: "))  # Example input
try:
    result = kaprekar_routine(input_number)
    print(f"Kaprekar routine steps for {input_number} to reach 6174 are: {result}")
except ValueError as e:
    print(e)