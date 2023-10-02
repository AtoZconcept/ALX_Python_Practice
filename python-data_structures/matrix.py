def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for a, num in enumerate(i):
            if a != len(i) - 1:
                print("{}".format(num), end=' ')
            else:
                print("{}".format(num), end="")
        print()
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()