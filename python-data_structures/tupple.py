def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        a1, a2 = (0, 0)
    elif len(tuple_a) == 1:
        a1, a2 = (tuple_a[0], 0)
    elif len(tuple_a) == 2:
        a1, a2 = tuple_a
    else:
        a1, a2, _ = tuple_a

    if len(tuple_b) == 0:
        b1, b2 = (0, 0)
    elif len(tuple_b) == 1:
        b1, b2 = (tuple_b[0], 0)
    elif len(tuple_b) == 2:
        b1, b2 = tuple_b
    else:
        b1, b2, _ = tuple_b

    new_tuple = (a1 + b1, a2 + b2)
    return new_tuple

tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))