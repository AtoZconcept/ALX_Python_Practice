def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return (a + b)


def sub(a, b):
    """My subtraction function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a - b
    """
    return (a - b)


def mul(a, b):
    """My multiplication function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a * b
    """
    return (a * b)


def div(a, b):
    """My division function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a / b
    """
    return int(a / b)

from sys import argv
count = len(argv) -1
if not count == 3:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)
a = argv[1]
b = argv[3]
operator = argv[2]
if operator == '+':
    print("{} + {} = {}".format(a, b, add(a, b)))
elif operator == '-':
    print("{} - {} = {}".format(a, b, sub(a, b)))
elif operator == '*':
    print("{} * {} = {}".format(a, b, mul(a, b)))
elif operator == '/':
    print("{} / {} = {}".format(a, b, div(a, b)))
else:
    print('Unknown operator. Available operators: +, -, * and /')
    exit(1)
exit (0)
