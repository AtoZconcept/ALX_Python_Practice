for num in range(100):
    end = '\n' if num == 99 else ', '
    print("{:02d}".format(num), end=end)

for alpha in range(ord('a'), ord('z') + 1):
    if chr(alpha) not in 'eq':
        end = '\n' if chr(alpha) == 'z' else ', '
        print("{:c}".format(alpha), end=end)
for i in range(9):
    for a in range(i + 1, 10):
        end = '\n' if i == 8 and a == 9 else ', '
        print("{:d}{:d}".format(i, a), end=end)

for i in range(99):
    print("{} = 0x{:x}".format(i, i))