#Таблица из цифр

n = int(input())
for i in range(n):
    for j in range(3):
        print(n, end=' ')
    print()

#
num = int(input())
n = num
while n > 0:
    print(num, num, num)
    n -=1
#
n = int(input())
for i in range(1,n+1):
    print(f"{n} {n} {n}")

#Таблица из цифр 2

n = int(input())
for i in range(1, n + 1):
    for j in range(5):
        print(i, end=" ")
    print()
#
x = int(input())
y = 0
for i in range(x):
    y += 1
    for j in range(5):
        print(y, end=' ')
    print()
#
n = int(input())
for i in range(1,n+1):
    print(f"{i} {i} {i} {i} {i}")
#3
[print(*(str(i)*5)) for i in range(1,int(input())+1)]

#Таблица из цифр 3

n = int(input())
for i in range(1, n + 1):
    for j in range(1, 10):
        print(f'{i} + {j} = {i + j}')
    print()
#
n = int(input())
for i in range(n):
    for j in range(9):
        print(i + 1, "+", j + 1, "=", i + j + 2)
    print()

