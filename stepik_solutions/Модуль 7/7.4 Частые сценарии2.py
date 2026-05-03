#Кол-во цисел

a = int(input())
b = int(input())
total = 0
for i in range(a, b + 1):
    if i**3 % 10 == 4 or i**3 % 10 == 9:
        total += 1
print(total)

#Сумма чисел

n = int(input())
total = 0
for i in range(n):
    num = int(input())
    total += num
print(total)

# #
n = int(input())
for i in range(n):
    total += int(input())
print(total)

#Асимптотическое приближение

from math import log
n = int(input())
total = 0
for i in range(1, n + 1):
    total += (1 / i)
print(total - log(n))

# #
import math
n = int(input())
harmonic_sum = sum(1 / i for i in range(1, n + 1))
result = harmonic_sum - math.log(n)
print(result)

#Сумма чисел 2

n = int(input())
total = 0
for i in range(n + 1):
    if i**2 % 10 == 2 or i**2 % 10 == 5 or i**2 % 10 == 8:
        total += i
print(total)

# #
n = int(input())
sm = 0
for i in range(5, n, 10):
    sm += i
print(sm)


#Факториал

n = int(input())
total = 1
for i in range(n):
    total *= (i + 1)
print(total)
#
n = int(input())
total = 1
for i in range(1, n + 1):
    total *= i
print(total)
#
from math import factorial as fac    #через math
print(fac(int(input())))

#Без нулей 0️


total = 1
for i in range(1, 11):
    num = int(input())
    if num != 0:
        total *= num
print(total)

#Сумма делителей

# n = int(input())
total = 0
for i in range(1, n + 1):
    if n % i == 0:
        total += i
print(total)

# # через математический алгоритм
n = int(input())
total = 0
for d in range(1, int(n ** 0.5) + 1):
    if n % d == 0:
        total += d
        if d != n // d:
            total += n // d
print(total)

