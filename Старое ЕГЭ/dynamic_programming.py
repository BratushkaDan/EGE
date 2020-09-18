n = int(input())
t = int(input())
tA = 0
tB = t

for i in range(n):
    a, b = [int(x) for x in input().split()]
    tA += a
    tB = min(tA + t, tB + b)
print(tB)
