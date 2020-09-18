n = int(input())
p = [0, 0]
p19 = [0, 0]

for i in range(n):
    x = int(input())
    if x % 19 == 0:
        if p19[x % 2] == 0:
            p19[x % 2] = x
        elif x > p19[x % 2]:
            p[x % 2] = max(p[x % 2], p19[x % 2])
            p19[x % 2] = x
        elif x > p[x % 2]:
            p[x % 2] = x
    else:
        p[x % 2] = max(x, p[x % 2])

if p19[0] * p[0] == 0 and p19[1] * p[1] == 0:
    print(0, 0)
elif p[0] * p19[0] < p[1] * p19[1]:
    print(p19[1], p[1])
else:
    print(p19[0], p[0])
    
