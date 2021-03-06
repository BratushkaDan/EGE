from math import e, sin, cos


def fn(x):
    return 2 * sin(7 * x) + 3 * cos(5 * x) * e ** (2 * x)


a, b = 0.5, 1.5
while b - a >= 10 ** -6:
    c = (a + b) / 2
    if fn(a) * fn(c) <= 0:
        b = c
    else:
        a = c

print(round(c, 6))
