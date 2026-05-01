# #
for i in range(4):
    j = i + 1
    print(i, j)
# #
six = 0
for i in range(27):
    j = i + 1
    print(i)
    if '7' in str(i):
        six += 1

print(j)
if '7' in str(j):
    six += 1
print(six)

#Повторяй за мной 2

n = input()
for i in range(10):
    print(i, n)
#
n = input()
print(*(f"{i} {n}" for i in range(10)), sep="\n")

#Квадрат числа

from math import pow
n = int(input())
for i in range(n+1):
    print('Квадрат числа', i, 'равен', int(pow(i, 2)))

#Звёздный треугольник

n = int(input())
if n >= 2:
    for i in range(n, -1, -1):
        print('*' * i)

n = int(input())
for i in range(n):
    print("*" * (n - i))

#Популяция

a = int(input())
b = int(input())
c = int(input())
for i in range(c):
    if i == 0:
        print(i + 1, a)
    else:
        a = (a * (1 + b / 100))
        print(i + 1, a)


a = int(input())
b = int(input())
c = int(input())
for i in range(c):
    m = a * (1 + b / 100) ** i
    print(i + 1, m)

a = int(input())
b = int(input())
c = int(input())
for i in range(c):
    print(1+i, a)
    a = a + (a / 100 * b)