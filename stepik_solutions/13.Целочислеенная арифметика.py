num = int(input())
a = num // 100
b = num // 10 % 10
c = num % 10
print(f'Сумма цифр = {a + b + c}\nПроизведение цифр = {a * b * c}')

num = int(input())
a = num // 100
b = num // 10 % 10
c = num % 10
print(a, b, c, sep='')
print(a, c, b, sep='')
print(b, a, c, sep='')
print(b, c, a, sep='')
print(c, a, b, sep='')
print(c, b, a, sep='')
print(f"{a} {b} {c}\n{a} {c} {b}\n{b} {a} {c}\n{b} {c} {a}\n{c} {a} {b}\n{c} {b} {a}")

num = int(input())
a = num // 1000
b = num // 100 % 10
c = num // 10 % 10
d = num % 10
print(f'Цифра в позиции тысяч равна {a}')
print(f'Цифра в позиции сотен равна {b}')
print(f'Цифра в позиции десятков равна {c}')
print(f'Цифра в позиции единиц равна {d}')