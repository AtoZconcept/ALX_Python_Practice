def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        for a, num in enumerate(i):
            new_matrix += num
        return new_matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)