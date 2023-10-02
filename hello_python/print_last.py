def print_last_digit(number):
    r = abs(number) % 10
    print("{}".format(r), end="")
    return r

print_last_digit(98)
print_last_digit(0)
r = print_last_digit(-1024)
print(r)