#Calculate the value of pi to a particular decimal points

import decimal
from decimal import Decimal, getcontext
import sys

def chudnovsky_algorithm(precision):
    """Calculate Pi using the Chudnovsky algorithm."""
    
    getcontext().prec = precision + 5  # Set precision slightly higher to avoid rounding errors
    
    C = 426880 * Decimal(10005).sqrt()
    K = 6
    M = 1
    X = 1
    L = 13591409
    S = L
    for i in range(1, precision):
        M = (K**3 - 16*K) * M // i**3
        L += 545140134
        X *= -262537412640768000
        S += Decimal(M * L) / X
        K += 12
    pi = C / S
    return pi

def main():
    # Get the desired number of decimal places from the command line
    if len(sys.argv) != 2:
        print("Usage: python calculate_pi.py <number_of_decimal_places>")
        return
    
    try:
        precision = int(sys.argv[1])
        if precision <= 0:
            raise ValueError("Precision must be a positive integer.")
    except ValueError as e:
        print(f"Error: {e}")
        return

    # Compute pi to the specified number of decimal places
    pi = chudnovsky_algorithm(precision)

    # Print the result with exactly the number of decimal places specified
    print(f"Pi to {precision} decimal places:\n{str(pi)[:precision+2]}")

if __name__ == "__main__":
    main()
