def no_c(my_string):
    new_string = ""
    for i in my_string:
        if i != 'C' and i != 'c':
            new_string += i
    return new_string
    
print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))