matrix = []
maximum = 0

# load data into matrix
with open('p11_input.txt', 'r') as f:
    for line in f:
        row = line.split(' ')
        row_numbers = []
        for element in row:
            row_numbers.append(int(element))
        matrix.append(row_numbers)

# get maximum product in the horizontal direction
for row in matrix:
    for i in range(0, 17):
        product = row[i] * row[i+1] * row[i+2] * row[i+3]
        if product > maximum:
            maximum = product

# get maximum product in the vertical direction
for c in range(0, 20):
    for r in range(0, 17):
        product = matrix[r][c] * matrix[r+1][c] * matrix[r+2][c] * matrix[r+3][c]
        if product > maximum:
            maximum = product

# get maximum product in the first diagonal direction (bottom-left to top-right)
for r in range(3, 20):
    for c in range(0, 17):
        product = matrix[r][c] * matrix[r-1][c+1] * matrix[r-2][c+2] * matrix[r-3][c+3]
        if product > maximum:
            maximum = product

# get maximum product in the second diagonal direction (top-left to bottom-right)
for r in range(0, 17):
    for c in range(0, 17):
        product = matrix[r][c] * matrix[r+1][c+1] * matrix[r+2][c+2] * matrix[r+3][c+3]
        if product > maximum:
            maximum = product

print('Maximum product is {}.'.format(maximum))
