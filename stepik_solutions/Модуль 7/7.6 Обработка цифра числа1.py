#Обработка цифр числа с помощью цикла while
num = int(input())                                # считываем число
while num != 0:                                   # проверяем, что цифры числа не закончились
    last_digit = num % 10                         # получаем последнюю цифру числа
    ...                                           # обрабатываем последнюю цифру числа
    num = num // 10                               # удаляем последнюю цифру из числа

#находим чифру 7
num = 1576
has_seven = False                                 # сигнальная метка (флаг)

while num != 0:
    last_digit = num % 10
    if last_digit == 7:
        has_seven = True
    num = num // 10

if has_seven == True:
    print('YES')
else:
    print('NO')

#Обработка цифр числа с помощью цикла for
num = 8619
n = len(str(num))
for i in range(1, n + 1):
    digit = num // 10 ** (n - i) % 10
    print(i, '-я', ' цифра равна ', digit, sep='')