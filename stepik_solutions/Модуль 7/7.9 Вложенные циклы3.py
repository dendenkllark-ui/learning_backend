# Численный треугольник 1

n = int(input())
for i in range(1, n + 1):
    for j in range(i):
        print(i, end='')
    print()
#
n = int(input())
for i in range(1, n + 1):
    print(str(i) * i, end= " ")
    print()
#
n = int(input())
for i in range(1, n + 1):
    print(str(i) * i)
#
n = int(input())
counter = 1
for i in range(1, n + 1):
    for j in range(1):
        print(str(i) * counter)
        counter +=1

#Равнобедренный треугольник *

n = int(input())
if n % 2 == 1:
    for i in range(1, n):
        print("*" * i)
    for i in range(n, 0, -1):
        print("*" * i)

#
n = int(input())
mid = n // 2 + 1  
for i in range(1, mid + 1):
    for j in range(i):
        print('*', end='')
    print()
for i in range(mid - 1, 0, -1):
    for j in range(i):
        print('*', end='')
    print()
####
n = int(input())
middle = n // 2 + 1
for i in range(1, n + 1):
    # формула, которая сама уменьшает число после середины
    count = middle - abs(middle - i)
    print('*' * count)

##
n = int(input())
for i in range(1, n // 2 + 1):
    print('*' * i)
for i in range(n // 2 + 1, 0, -1):
    print('*' * i)