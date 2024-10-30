def find_valid_pairs(d):
    results = []
    # Define the range of 'a' (start of the series)
    for a in range(1, 10**(d-1)):  # to keep 'a' within d-1 digits
        # Define the range of 'b' (end of the series)
        for b in range(a + 1, 10**d):  # to keep 'b' within d digits
            n = b - a + 1  # Number of terms in the series
            series_sum = (n * (a + b)) // 2  # Sum of the series
            concat_number = a * 10**d + b  # Concatenated number
            if series_sum == concat_number:
                results.append((a, b))
                
    return results

# Example usage for 2-digit 'b'
valid_pairs = find_valid_pairs(3)
print(valid_pairs)
