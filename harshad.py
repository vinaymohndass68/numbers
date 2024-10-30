def is_harshad(n):
    # Calculate the sum of the digits of n
    digit_sum = sum(int(digit) for digit in str(n))
    
    # Check if the number is divisible by the sum of its digits
    return n % digit_sum == 0

def find_harshad_numbers(limit):
    harshad_numbers = []
    for num in range(1, limit + 1):
        if is_harshad(num):
            harshad_numbers.append(num)
    return harshad_numbers

# Specify the range you want to search for Harshad numbers
limit = 1000  # You can change this limit
harshad_numbers = find_harshad_numbers(limit)

print("Harshad numbers up to", limit, "are:", harshad_numbers)