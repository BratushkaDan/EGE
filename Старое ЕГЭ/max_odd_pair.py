n = int(input())
l = 6
maxi = [0, 0]
s = 0
Q = [int(input()) for i in range(l)]

for i in range(l, n):
    x = int(input())
    y = Q[i % l]
    Q[i % l] = x

    maxi[y % 2] = max(maxi[y % 2], y)
    if maxi[(x+1) % 2] != 0:
        s = x + maxi[(x+1) % 2]

print(s)
