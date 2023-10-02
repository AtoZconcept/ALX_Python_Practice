from sys import argv
list = argv[1:]
add = 0
for arg in list:
    add += int(arg)
print("{}".format(add))