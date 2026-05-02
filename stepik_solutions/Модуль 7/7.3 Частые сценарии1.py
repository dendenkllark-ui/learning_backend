
#Подсчёт количества

counter = 0                                             # создаём переменную счётчика
for _ in range(10):
    num = int(input())
    if num > 10:                                        # при выполнении условия 
        counter = counter + 1                           # увеличиваем значение cчётчика

print('Было введено', counter, 'чисел, больших 10.')

#

counter1 = 0
counter2 = 0
for _ in range(10):
    num = int(input())
    if num > 10:
        counter1 = counter1 + 1
    if num == 0:
        counter2 = counter2 + 1

print('Было введено', counter1, 'чисел, больших 10.')
print('Было введено', counter2, 'нулей.' )

#

counter = 0
for i in range(1, 101):
    if i**2 % 10 == 4:
        counter = counter + 1

print(counter)

#Вычисление суммы и произведения

total = 0
for _ in range(10):
    num = int(input())
    if num > 10:
        total = total + num

print('Сумма чисел больших 10 равна',  total)

#

total = 0
for i in range(1, 101):
    total = total + i

print('Сумма равна', total)

#

total = 0
for _ in range(10):
    num = int(input())
    total = total + num

average = total / 10
print('Среднее значение равно', average)

#Максимум и минимум

largest = 0
for _ in range(10):
    num = int(input())    
    if num > largest:
        largest = num

print('Наибольшее число равно', largest) 

#

largest = int(input())  # принимаем первое число за максимальное
for _ in range(9):
    num = int(input())
    if num > largest:
        largest = num

print('Наибольшее число равно', largest) 

#Обмен значений переменных

temp = x
x = y
y = temp
#
x, y = y, x
#
a, b, c, d = 1, 2, 3, 4
a, b, c, d = b, c, d, a
print(a, b, c, d)
#
a, b = 3, 4
a, b = a + b, 2 * a
print(a, b)

#Расширенные операторы присваивания

total += num

#Сигнальные метки

#Число простое или составное?
num = int(input())
flag = True

for i in range(2, num):
    if num % i == 0:  #  если исходное число делится на какое-либо отличное от 1 и самого себя
        flag = False

if num == 1:
    print('Это единица, она не простая и не составная') 
elif flag == True:
    print('Число простое')
else:
    print('Число составное')
