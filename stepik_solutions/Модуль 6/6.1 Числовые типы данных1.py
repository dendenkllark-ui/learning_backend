#Площадь треугольника

a = float(input())
b = float(input())
s = 0.5 * a * b
print(s)

#Две старушки

s = float(input())
v1 = float(input())
v2 = float(input())
t = s / (v1 + v2)
print(t)

#Обратное число

a = float(input())
if a != 0:
    print(a**(-1))
else:
    print('Обратного числа не существует')

#451 градус по Фаренгейту

a = float(input())
t = 5 / 9 * (a - 32)
print(t)

#Dog age

a = int(input())
n = 10.5
b = a * n
if a <= 2:
    b = a * 10.5
    if b % 1 == 0:
        print(int(b))
    else:
        print(b)
elif a > 2:
    b = b - 6.5 * (a-2)
    if b % 1 == 0:
        print(int(b))
    else:
        print(b)


a = int(input())
if a <= 2:
    b = a * 10.5
else:
    b = 21 + (a - 2) * 4
if b % 1 == 0:
    print(int(b))
else:
    print(b)

#Первая цифра после точки

a = float(input()) * 10 % 10
print(int(a)) 

#Дробная часть

a = float(input()) % 1
print(a)

a = float(input())
print(a - int(a))