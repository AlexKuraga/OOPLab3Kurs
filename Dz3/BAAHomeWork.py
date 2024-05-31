def ef(q, h, r, p):
    return (9.81 * r * q * h) / (p * 1000)


def pN(q, h, r, p, p_n, f1):
    return (9.81 * r * q * h) / (p_n * f1(q, h, r, p) * 1000)


def function1(f1, f2):
    def function2(q, h, r, p, p_n):
        if p_n is None:
            return f1(q, h, r, p)
        else:
            return f2(q, h, r, p, p_n, f1)
    return function2

print(function1(ef, pN)(12, 12, 3, 5, 12))
