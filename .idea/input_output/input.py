filename = "text.txt"
with open(filename, mode='w', encoding='utf-8') as file:
    file.write("The name of my school ALX")

with open(filename, mode='a+', encoding='utf-8') as file:
    file.write("\nWe do hard things")

with open(filename, mode='r', encoding='UTF-8') as file:
    char_len = file.read()
for i in char_len:
    print(i, end='')
print("\nThe number of the characters: {}".format(len(char_len)))
