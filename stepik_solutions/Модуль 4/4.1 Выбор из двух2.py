a = input()
b = input()
if a == b:
    print("Пароль принят")
else:
    print("Пароль не принят")

a = int(input())
if a % 2 == 0:
    print("Четное")
else:
    print("Нечетное")

a = int(input())
if a >= 18:
    print("Доступ разрешен")
else:
    print("Доступ запрещен")

a = int(input())
b = int(input())
if a > b:
    print(b)
else:
    print(a)
a = int(input())
b = int(input())
c = int(input())
if c - b == b - a:
    print("YES")
else:
    print('NO')