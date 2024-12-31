def generate_pascals_triangle(n):
    triangle = []

    for i in range(n):
        row = [1] * (i + 1)  # Start with a row of 1s
        if i > 1:  # Calculate the values for interior elements
            for j in range(1, i):
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    
    return triangle

def display_pascals_triangle(triangle):
    for row in triangle:
        print(' '.join(map(str, row)).center(len(triangle[-1]) * 2))  # Center the rows for better display

# Specify the number of rows

num_rows = int(input("Enter the number of limit: "))  # You can change this value
pascals_triangle = generate_pascals_triangle(num_rows)

print("Pascal's Triangle:")
display_pascals_triangle(pascals_triangle)