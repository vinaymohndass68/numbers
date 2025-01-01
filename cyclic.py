'''A happy number is a number that eventually reaches 1 when you repeatedly replace it with the 
sum of the squares of its digits. If the process results in 1, the number is considered happy; 
otherwise, it is an unhappy number, leading to a loop or cycle.

'''

def is_cyclic_number(n):
    """Check if a number is a cyclic number by verifying cyclic permutations when multiplied by integers."""
    # Convert number to a string to easily manipulate digits
    str_n = str(n)
    length = len(str_n)
    
    # Generate cyclic permutations of the number
    cyclic_permutations = {str_n[i:] + str_n[:i] for i in range(length)}
    
    # Check if all products of n * (1, 2, ..., length) are cyclic permutations
    for i in range(1, length + 1):
        product = str(n * i)
        
        # If the product is not a cyclic permutation of the original number, return False
        if product not in cyclic_permutations:
            return False
    
    return True

def find_cyclic_numbers(limit):
    """Find all cyclic numbers up to a given limit."""
    cyclic_numbers = []
    
    for n in range(1, limit + 1):
        if is_cyclic_number(n):
            cyclic_numbers.append(n)
    
    return cyclic_numbers

# Set a limit to search for cyclic numbers (example: limit 2000000)
limit = int(input("Enter the limit: "))
cyclic_numbers = find_cyclic_numbers(limit)

print(f"Cyclic numbers up to {limit}: {cyclic_numbers}")