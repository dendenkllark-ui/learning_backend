
#Считывание данных до стоп значения

text = input()
total = 0
while text != 'stop':
    total += int(text)
    text = input()
print('Сумма чисел равна', total)

#
num = int(input())
counter = 0
while '0' not in str(num):
    counter += 1
    num = int(input())
print(counter)

#
num = int(input())
total = 0
while num > -4:
    num = int(input())
    total += num

#До КОНЦА 1

text = input()
while text != 'КОНЕЦ':
    print(text)
    text = input()

#
while True:
    word = input()
    if word == 'КОНЕЦ':
        break
    print(word)

#До КОНЦА 2

text = input()
while text != 'КОНЕЦ' and text != 'конец':
    print(text)   
    text = input()
#
while True:
    word = input()
    if word == 'КОНЕЦ' or word == 'конец':
        break
    print(word)
#
word = input()
while not (word == "КОНЕЦ" or word == "конец"):
    print(word)
    word = input()
#
word = input()
while 'КОНЕЦ' != word != 'конец':
    print(word)
    word = input()
#
while (word := input()) not in ('КОНЕЦ', 'конец'):
    print(word)


#Количество членов

stop = ['стоп', 'хватит', 'достаточно']
text = input()
total = 0
while text not in stop:
    total += 1
    text = input()
print(total)

#
STOP = {'стоп', 'хватит', 'достаточно'}
count = 0
while (word := input()) not in STOP:
    count += 1
print(count)

#Пока делимся

num = int(input())
while num % 7 == 0:
    print(num)
    num = int(input())
#
while True:
    a = int(input())
    if a % 7 != 0:
        break
    print(a)
#
while True:
    x = int(input())
    if x % 7 != 0:
        break
    print(x)

    
#Сумма чисел

num = int(input())
sum = 0
while num >= 0:
    sum += num
    num = int(input())
print(sum)
#
s = 0
while True:
    a = int(input())
    if a < 0:
        break
    s += a
print(s)