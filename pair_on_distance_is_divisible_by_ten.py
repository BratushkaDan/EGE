n = int(input())
l = 10
Q = [int(input()) for i in range(l)]
d2, d5, d10 = 0, 0, 0
c = 0

for i in range(l, n):
    x = int(input())
    y = Q[i % l]
    Q[i % l] = x

    if y % 10 == 0:
        d10 += 1
    elif y % 5 == 0:
        d5 += 1
    elif y % 2 == 0:
        d2 += 1
    if x % 10 == 0:
        c += i - l + 1
    elif x % 5 == 0:
        c += d2 + d10
    elif x % 2 == 0:
        c += d5 + d10
    else:
        c += d10
print(c)
