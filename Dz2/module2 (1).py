import math

def rat_operation(a, b, operation):
    x = (a, b)
    if operation == 'numer':
        g = math.gcd(x[0], x[1])
        return x[0] / g
    elif operation == 'denom':
        g = math.gcd(x[0], x[1])
        return x[1] / g
    else:
        raise ValueError("ERROR")

try:
    a = int(input("Enter the numerator: "))
    b = int(input("Enter the denominator: "))
    result = rat_operation(a, b, 'numer')
    print("Numerator:", result)
    result = rat_operation(a, b, 'denom')
    print("Denominator:", result)
except ValueError:
    print("Invalid input.")
