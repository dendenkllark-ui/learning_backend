

# Найти гипотенузу по Пифагору 

def compute_hypotenuse(a, b):
    c = (a ** 2 + b ** 2) ** 0.5
    return c                

print(compute_hypotenuse(3, 4))
print(compute_hypotenuse(5, 12))
print(compute_hypotenuse(1, 1))
#Если нужно передать программе числа, считанные с клавиатуры, то мы пишем следующий код:
x = int(input())
y = int(input())
hypotenuse = compute_hypotenuse(x, y)
print(hypotenuse)



#В модуле math имеется встроенная функция hypot(x, у) которая возвращает 
# длину гипотенузы прямоугольного треугольника с катетами x и y.

#Найти расстояние мжеду двумя точками на поле координат

import math  # Импортируем математический модуль
def compute_hypotenuse(a, b):
    # Эта функция принимает два катета и возвращает гипотенузу
    return math.hypot(a, b)
def get_distance(x1, y1, x2, y2):
    # Эта функция считает два катета и передает значение параметров в функцию выше
    return compute_hypotenuse(x1 - x2, y1 - y2)
x1, y1 = float(input()), float(input())  # считываем координаты первой точки
x2, y2 = float(input()), float(input())  # считываем координаты второй точки

print(get_distance(x1, y1, x2, y2))      # вычисляем и выводим расстояние между точками


#Напишите функцию sum_digits(n), принимающую в качестве аргумента 
# натуральное число и возвращающую сумму его цифр.

def sum_digits(n):
    result = 0
    while n > 0:
        result += n % 10
        n //= 10
    return result
n = int(input())
print(sum_digits(n)) 

# Вывести среднее значение элементов списка

def compute_average(numbers):
    return sum(numbers) / len(numbers)
numbers = [1, 3, 5, 1, 6, 8, 10, 2]
print(compute_average(numbers))
