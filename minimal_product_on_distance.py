n = int(input())
l = 6
Q = [int(input()) for i in range(l)]
lprod = 1000001
least = [1001, 1001]  # [even, odd]

for i in range(l, n):
    x = int(input())
    y = Q[i % l]
    Q[i % l] = x

    least[y % 2] = min(least[y % 2], y)
    if (least[0] * x) % 2 == 0 and (least[1] * x) % 2 == 0:
        lprod = min(lprod, least[0] * x, least[1] * x)
    elif (least[0] * x) % 2 == 0:
        lprod = min(lprod, least[0] * x)
    elif (least[1] * x) % 2 == 0:
        lprod = min(lprod, least[1] * x)
if lprod == 1000001 or (least == [1001, 1001]):
    print(-1)
else:
    print(lprod)
