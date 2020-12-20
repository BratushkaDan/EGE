c, d1, d2, d17, d34 = [0] * 5

for x in file:
    if x % 34 == 0:
        c += d1
        d34 += 1
    elif x % 17 == 0:
        c += d34 + d2
        d17 += 1
    elif x % 2 == 0:
        c += d34 + d17
        d2 += 1
    else:
        c += d34
    d1 += 1
print(c)
