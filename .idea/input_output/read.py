filename = "text.txt"
with open(filename, mode='r', encoding='utf-8') as file:
    for i in file:
        print(i, end="")
    print()