for i in range(0):
    print('Привет')

for i in range(5):
    num = int(input())
    print('Квадрат вашего числа', num, 'равен:', num * num)
print('Цикл завершен')

#Сначала вводим 5 чифр, потом получаем 5 ответов

numbers = []
for i in range(5):
   num = int(input())
   numbers.append(num) #Добавляем в конец списка
for n in numbers:
    print('Квадрат вашего числа', n, 'равен:', n * n)
print('Цикл завершен')
#
num = 0
for i in range(2):
    num = num + int(input())

#Задача 1

for i in range(10):
    print('Python is awesome!')

#Последовательность символов

for i in range(6):
    print('AAA')
for i in range(5):
    print('BBBB')
print('E')
for i in range(9):
    print('TTTTT')
print('G')

chars  = ['A', 'B', 'E', 'T', 'G']
widths = [3, 4, 1, 5, 1]
heights= [6, 5, 1, 9, 1]

for i in range(len(chars)):
    for _ in range(heights[i]):
        for _ in range(widths[i]):
            print(chars[i], end='')
        print()

#Повторяй за мной 1


a = input()
b = int(input())
for i in range(b):
    print(a) 

#Звёздный прямоугольник v

n = int(input())
if 1 <= n <= 20:
    for i in range(n):
        print('*' * 19)