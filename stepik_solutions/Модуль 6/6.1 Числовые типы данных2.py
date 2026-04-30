#Наименьшее и наибольшее

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
print('Наименьшее число =', min(a, b, c, d, e))
print('Наибольшее число =', max (a, b, c, d, e))

a = [] 
for _ in range(5):
    n = int(input())
    a.append(n)

print('Наименьшее число =', min(a))
print('Наибольшее число =', max(a))

a = [int(input()) for _ in range(5)]
print('Наименьшее число =', min(a))
print('Наибольшее число =', max(a))

#Абсолютная сумма

a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
print(abs(a) + abs(b) + abs(c) + abs(d) + abs(e))

a = [float(input()) for _ in range(5)]
print(sum(abs(n) for n in a))

a = [float(input()) for _ in range(5)]
print(sum(map(abs, a)))

#Интересное число

n = int(input())
a = n // 100
b = (n // 10) % 10
c = n % 10
if (max(a, b, c) - min(a, b, c)) == ((a + b + c) - max(a, b, c) - min(a, b, c)):
    print('Число интересное')
else:
    print('Число неинтересное')

n = int(input())
a = n // 100 % 10
b = n // 10 % 10
c = n // 1 % 10
if a + b == c or b + c == a or c + a == b:
    print('Число интересное')
else:
    print('Число неинтересное')

#Сортировка трех

a = int(input())
b = int(input())
c = int(input())
print(max(a, b, c), ((a + b + c) - max(a, b, c) - min(a, b, c)), min(a, b, c), sep='\n')

a = [int(input()), int(input()), int(input())]
a.sort(reverse=True)
print(*a, sep='\n')

a = [int(input()) for _ in range(3)]
a.sort(reverse=True)
print(*a, sep='\n')

#Манхэттенское расстояние

a = int(input())
b = int(input())
c = int(input())
d = int(input())
s = abs(a - c) + abs(b - d)
print(s)

a = [int(input()) for _ in range(4)]
s = abs(a[0] - a[2]) + abs(a[1] - a[3])
print(s)

a = [int(input()) for _ in range(4)]
x1, y1, x2, y2 = a
s = abs(x1 - x2) + abs(y1 - y2)
print(s)

x1, y1, x2, y2 = [int(input()) for _ in range(4)]
print(abs(x1 - x2) + abs(y1 - y2))

#Как автоматически выдавать ответ с дробью или без

a = int(input()) / 2
print(a)    #Вот тут будет всегда дробное число

a = int(input()) / 2
print(f"{a:g}")

a = int(input()) / 2
if a.is_integer():
    print(int(a))  # Превращаем в целое перед выводом
else:
    print(a)       # Оставляем как есть

n = int(input())
if n % 2 == 0:
    print(n // 2)  
else:
    print(n / 2)   