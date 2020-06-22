n = int(input())
d = 12 + 1
a = [0] * d

for i in range(n):
    a[int(input())] += 1

tasks = list(range(d))
for i in range(n):
    for k in range(d - 1 - i):
        if a[k] > a[k + 1]:
            a[k], a[k + 1] = a[k + 1], a[k]
            tasks[k], tasks[k + 1] = tasks[k + 1], tasks[k]

for i in range(d):
    if not a[i] == 0:
        print(tasks[i], a[i])
