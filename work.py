import sys

def quadratic(arguments: list[float]):
    if len(arguments) < 3:
        return "Not valid"
    a = arguments[0]
    b = arguments[1]
    c = arguments[2]
    x = b**2 - 4*a*c
    if x < 0:
        return "Discriminant cannot be negative"
    root1 = (-b + x**0.5)/2*a
    root2 = (-b - x**0.5)/2*a
    return root1, root2

def derivative(arguments: list[float]):
    #This is very hard to program actually
    raise NotImplementedError

def multiply(arguments: list[float]):
    if not arguments:
        return 1
    total = arguments[0]
    for arg in arguments[1:]:
        total *= arg
    return total

def divide(arguments: list[float]):
    if not arguments:
        return 1
    total = arguments[0]
    for arg in arguments[1:]:
        total /= arg
    return total

if __name__ == '__main__':
    stuff= [float(arg) for arg in sys.argv[1:]]
    print(quadratic(stuff))