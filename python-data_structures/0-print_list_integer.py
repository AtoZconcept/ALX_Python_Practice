def print_list_integer(my_list=[]):
    for i in my_list:
        print("{}".format(i))

def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]

my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)

my_list = [1, 2, 3, 4, 5]
idx = 3
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))


def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        my_list.pop(idx)
        my_list.insert(idx, element)
        return my_list    
    

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = replace_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)

def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return
    for i in reversed(my_list):
        print("{}".format(i))

my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)

def new_in_list(my_list, idx, element):
    my_list = new_list
    if idx < 0 or idx >= len(my_list):
        return new_list
    else:
        new_list.pop(idx)
        new_list.insert(idx, element)
        return new_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = new_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)
