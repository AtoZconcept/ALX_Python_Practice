def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print('FizzBuzz', end=' ')
        elif num % 3 == 0:
            print('Fizz', end=' ')
        elif num % 5 == 0:
            print('Buzz', end=' ')
        else:
            print("{:d}".format(num), end=' ')
        #print(' ')
       
#fizzbuzz = __import__('12-fizzbuzz').fizzbuzz

fizzbuzz()
print("")