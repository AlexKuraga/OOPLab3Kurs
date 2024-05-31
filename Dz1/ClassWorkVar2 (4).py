def calculate_term(n):
    return n / ((1 + 2*n)**3)

def sum(a, b):
    return a + b

def calculate_series(a, b):
    if a == b:
        return calculate_term(a)
    else:
        return sum(calculate_term(a), calculate_series(a-1, b))

def res():
    n = 5
    k = 2
    print (calculate_series (n, k))

res()
