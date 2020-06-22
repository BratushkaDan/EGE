diff = 10000
s = 0

for i in range(int(input())):
    x, y = list(map(int, input().split()))
    if diff > abs(x-y) > 0:  # diff > abs(x-y) and abs(x-y) % 2 != 0 - если требуется, чтобы сумма была четна/нечетна
        diff = abs(x-y)
    s += max(x, y)

if diff == 10000:
    print(0)
elif s % 3 == 0:
    print(s-diff)
else:
    print(s)
