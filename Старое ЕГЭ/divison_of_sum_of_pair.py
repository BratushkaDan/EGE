mod = [0] * 117
s, p = 0, [0, 0]
for i in range(int(input())):
    x = int(input())
    # 1: к числу есть пара, 2: сумма пары больше суммы предыдущей, 3: предыдущее число больше текущего
    if mod[(117-x) % 117] != 0 and x + mod[(117-x) % 117] > s and mod[(117-x) % 117] > x:
        s = x + mod[(117-x) % 117]
        p = [x, mod[(117-x) % 117]]
    mod[x % 117] = max(mod[x % 117], x)

if p == [0, 0]:
    print('NO')
else:
    print(*p)
