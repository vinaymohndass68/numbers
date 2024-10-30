def is_kaprekar(n):
    # Square the number
    square = n * n
    str_square = str(square)
    len_n = len(str(n))

    # Split the square into two parts
    right_part = str_square[-len_n:]  # Rightmost digits
    left_part = str_square[:-len_n] if str_square[:-len_n] != '' else '0'  # Leftmost digits

    # Sum the two parts and check if it equals the original number
    if n == int(left_part) + int(right_part):
        return True
    return False

def find_kaprekar_numbers(limit):
    kaprekar_numbers = []
    for num in range(1, limit + 1):
        if is_kaprekar(num):
            kaprekar_numbers.append(num)
    return kaprekar_numbers

# Specify the range you want to search for Kaprekar numbers
limit = 100000  # You can change this limit
kaprekar_numbers = find_kaprekar_numbers(limit)

print("Kaprekar numbers up to", limit, "are:", kaprekar_numbers)