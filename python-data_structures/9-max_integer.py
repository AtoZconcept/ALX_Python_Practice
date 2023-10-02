def max_integer(my_list=[]):
    if not list:
        return None
    else:
        max = my_list[0]
        for i in my_list:
            if i > max:
                max = i
        return max
my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))