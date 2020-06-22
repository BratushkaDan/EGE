n = int(input())
l = 4
Q = [int(input()) for i in range(l)]
k = 0
k29 = 0

for i in range(l, n):
    x = int(input())
    y = Q[i % l]
    Q[i % l] = x
    if y % 29 == 0:
        k29 += 1
    if x % 29 == 0:
        k += i - l + 1
    else:
        k += k29
print(k)
