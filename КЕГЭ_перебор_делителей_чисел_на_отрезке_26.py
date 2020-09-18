a = 174457
b = 174505

for i in range(a, b + 1):
    rs = []
    for k in range(2, int(i / 2) + 1):
        if len(rs) > 2:
            break
        if i % k == 0:
            rs.append(k)
    if len(rs) == 2:
        print(i, *rs)
