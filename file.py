A = [1, 2, 3]
B = [4, 5]
print((B + A) * 2)  # [4, 5, 1, 2, 3, 4, 5, 1, 2, 3]

a = [1, 2, 3]
b = a * 1
b.pop()
print(b, a)  # [1, 2] [1, 2, 3]

a = [1, 2, 3]
b = a
b.pop()
print(b, a)  # [1, 2] [1, 2]

# массив из n нулей:
n = int(input())
Arr = [0] * n

# print(0b1101, -0b1101)  # 13, -13
# print(bin(13))  # 0b1101
# print(0o77, oct(0o77))  # 63, 0o77
# print(0xFF, 0xff, hex(255))  # 255, 255, 0xff


def foo(x, y):
    print('x: {}, y: {}'.format(x, y))


foo(1, 2)  # x: 1, y: 2
foo(y=2, x=1)  # x: 1, y: 2

print(*range(0, 3))  # 0 1 2
print(*"Hello", sep='--')  # H--e--l--l--o
# * unpacks arguments from iterable object

A = list(range(10, 60, 10))
print(A)  # [10, 20, 30, 40, 50]
x, y, *other = A  # 10 20 [30, 40, 50] — here can be given only 2 values from list A
*other, x, y = A  # [10, 20, 30] 40 50

strings = ['1', '2', '45', '2']
numbers = [int(x) for x in strings]
numbersToo = list(map(int, strings))
line = list(map(float, input().split()))

is_all_even = True
is_any_negative = False
for i in range(int(input())):
    n = int(input())
    is_all_even &= n % 2 == 0
    is_any_negative |= n < 0

sum(randint(1, 10) for k in range(0, 10))
max(a, b)  # at least 2 variables or iterable object
min(x, y)  # at least 2 variables or iterable object

iterable = 'any array, or string etc.'
iterable.find(',')  # finds index of the char or the element

# помнить про ссылочную модель данных в python - список должен копироваться explicitly

print(ord('f'))  # 102
print(chr(102))  # 'f'

a, b = [x for x in input().split()]
foo, bar = [1, 2]  # foo = 1, bar = 2

# Циклическая очередь:
l = 3  # Длина очереди
Q = [int(input()) for i in range(l)]

for i in range(l, int(input())):
    x = int(input())
    y = Q[i % l]
    Q[i % l] = x

abs(x - y)  # doesn't require imported module math

Arr = [int(input()) for i in range(int(input()))]
# k = 0
# for b in a:
#     if len(hex(b)[2:]) == len(str(b)):
#         k += 1
# print(k)
print(*(m for m in a if m % 10 == m % 16))
print(max((m for m in Arr if m % 10 == m % 16), default=0))

a = [1, 2, 3, 4]
print('a[2:]', a[2:])  # [3, 4]
print('a[2:3]', a[2:3])  # [3]
print('a[-1]', a[-1])  # 4
print('a[-1:1]', a[-1:1])  # []
print('a[1:-1]', a[1:-1])  # [2, 3]
print('a[:-1]', a[:-1])  # [1, 2, 3]
print('a[1:4]', a[1:4])  # [2, 3, 4]
print('a[-4:-2]', a[-4:-2])  # [1, 2]
