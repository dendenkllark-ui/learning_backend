
#Последовательность чисел 1

a = int(input())
b = int(input())
for i in range(a, b + 1):
    print(i)

#Таблица умножения

n = int(input())
for i in range(1, 11):
    print(n, 'x', i, '=', n * i)

n = int(input())
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

p = int(input())
print(*[f'{p} x {i} = {i * p}' for i in range(1, 11)], sep="\n")

#Последовательность чисел 2

a = int(input())
b = int(input())
for i in range(a, b + 1):
    if i % 17 == 0 or i % 10 == 9 or ( i % 3 == 0 and i % 5 == 0):    # (i % 3 == 0 and i % 5 == 0) можно наменить как i % 15 == 0
        print(i)

#Последовательность чисел 3

a = int(input())
b = int(input())
for i in range(a, b - 1, -1):
    if i % 2 != 0:
        print(i)

m = int(input())
n = int(input())
#превращаем m в нечётное
m = m - (m + 1) % 2  # для чётных даёт m-1, для нечётных оставляет m
for i in range(m, n - 1, -2):
    print(i)


#Последовательность чисел 4

m = int(input())
n = int(input())
if m < n:
    for i in range (m, n + 1):
        print(i)
else:
    for i in range (m, n - 1, -1):
        print(i)
#
m = int(input())
n = int(input())
step = 1 if m < n else -1
for i in range(m, n + step, step):
    print(i)
#
m = int(input())
n = int(input())
r = range(m, n + (1 if m < n else -1), 1 if m < n else -1)
print(*r, sep="\n")