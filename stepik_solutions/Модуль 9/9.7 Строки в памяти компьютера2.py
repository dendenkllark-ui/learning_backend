## Определить слебующуб букву
n = input()
for i in range(33):
    if n != "Я":
        print(chr(ord(n) + 1))
        break
    else:
        print("Дальше букв нет")
        break

#
a = input()
if a == "Я":
    print("Дальше букв нет")
else:
    b = ord(a) + 1
    print(chr(b))


# Опеределить буквы в заданном диапазоне кодового значения

a = int(input())
b = int(input())
for i in range(a, b + 1):
    print(chr(i), end=' ')

# Перевести каждый символ строки в код из unicide

a = input()
for i in a:
    i = ord(i)
    print(i, end=' ')

# Найти суммы кодов строки и вывести самую большую

a = input()
b = input()
c = input()
d = input()
x1 = 0
x2 = 0
x3 = 0
x4 = 0
for i in a:
    i = ord(i)
    x1 += i
for i in b:
    i = ord(i)
    x2 += i
for i in c:
    i = ord(i)
    x3 += i
for i in d:
    i = ord(i)
    x4 += i
if max(x1, x2, x3, x4) == x1:
    print(a)
elif max(x1, x2, x3, x4) == x2:
    print(b)
elif max(x1, x2, x3, x4) == x3:
    print(c)
else:
    print(d)

###
heaviest_word = ''
max_heaviness = 0
for _ in range(4):
    cur_word = input()
    cur_heaviness = 0
    for c in cur_word:
        cur_heaviness += ord(c)
    if cur_heaviness > max_heaviness:
        heaviest_word = cur_word
        max_heaviness = cur_heaviness
print(heaviest_word)

##
strings = [input() for _ in range(4)]
# Находим и печатаем лучшую строку
print(max(strings, key=lambda s: sum(ord(c) for c in s)))


