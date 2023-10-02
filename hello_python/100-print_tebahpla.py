value = 0
asc = 122
for num in range(1, 27):
    if num % 2 == 0:
        value = asc - 32
    else:
        value = asc
    asc -= 1
    print("{:c}".format(value), end='')