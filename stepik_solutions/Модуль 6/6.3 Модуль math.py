# import math

# num1 = math.sqrt(2)     # вычисление квадратного корня из двух
# num2 = math.ceil(3.8)   # округление числа вверх
# num3 = math.floor(3.8)  # округление числа вниз

# print(num1)
# print(num2)
# print(num3)

#Чтобы везде не указывать вызов модулей

# from math import *

# num1 = sqrt(2)     # вычисление корня квадратного из двух
# num2 = ceil(3.8)   # округление числа вверх
# num3 = floor(3.8)  # округление числа вниз

# print(num1)
# print(num2)
# print(num3)

#Площадь и длина

from math import pow, pi
r = float(input())
print((pi * pow(r, 2)), 2 * pi * r, sep='\n')

#Пол и потолок

from math import floor, ceil
x = float(input())
print(floor(x) + ceil(x))

#Евклидово расстояние

from math import sqrt, pow
x1, y1, x2, y2 = [float(input()) for _ in range(4)]
print(sqrt(pow(x1-x2, 2) + pow(y1-y2, 2))) 

#Тригонометрическое выражение

from math import pow, sin, cos, tan, radians
x = float(input())
x = radians(x)
print(sin(x) + cos(x) + pow(tan(x), 2))

#Правильный многоугольник 

from math import pow, pi, tan
n, a = [float(input()) for _ in range(2)]
print((n * pow(a, 2)) / (4 * tan(pi / n)))

#Средние значения

from math import pow, sqrt
a, b = [float(input()) for _ in range(2)]
print((a + b) / 2, sqrt(a * b), (2 * a * b) / (a + b), sqrt((pow(a, 2) + pow(b, 2)) / 2), sep='\n')

#Квадратное уравнение

from math import pow, sqrt
a, b, c = [float(input()) for _ in range(3)]
if a != 0:
    D = pow(b, 2) - 4 * a * c
    if D < 0:
        print('Нет корней')
    elif D == 0:
        print(-b / (2 * a))
    else:
        x1 = (-b - sqrt(D)) / (2 * a)
        x2 = (-b + sqrt(D)) / (2 * a)
        print(min(x1, x2), max(x1, x2), sep='\n')
