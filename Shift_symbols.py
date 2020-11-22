# Если нужно сдвигать символы на сколько-то
a = 'abcdefghijklmnopqrstuvwxyz'
st = input()
nstr = ''
l = 0
for i in range(len(st)):
    if st[i].lower() in a:
        l += 1
    else:
        for k in range(i - l, i):
            oldpos = a.find(st[k].lower())
            nstr += a[(oldpos + l) % 26] if st[k].lower() == st[k] else a[(oldpos + l) % 26].upper()
        nstr += st[i]
        l = 0
    if st[i] == '#': break
print(nstr)
