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

