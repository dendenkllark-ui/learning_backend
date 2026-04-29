# Задача про кратность года
a = int(input())
if a % 100 == 0:
    print('YES')
else:
    print('NO')

#Задача пол шахматную доску

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (x1 + y1) % 2 == 0 and (x2 + y2) % 2 == 0:
    print('YES')
elif (x1 + y1) % 2 != 0 and (x2 + y2) % 2 != 0:
    print('YES')
else:
    print('NO')


x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (x1 + y1) % 2 == (x2 + y2) % 2:
    print('YES')
else:
    print('NO')

#Задача про девочек в команде

a = int(input())
b = input()
if 10 <= a <=15 and b == 'f':
    print('YES')
else:
    print('NO')

#Задача про римские цифры

a = int(input())
if 1 <= a <= 10:
    if a == 1:
        print('I')
    elif a == 2:
        print('II')
    elif a == 3:
        print('III')
    elif a == 4:
        print('IV')
    elif a == 5:
        print('V')
    elif a == 6:
        print('VI')
    elif a == 7:
        print('VII')
    elif a == 8:
        print('VIII')
    elif a == 9:
        print('IX')
    elif a == 10:
        print('X')
else:
    print('ошибка')


a = int(input())
rim = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']

if 1 <= a <= 10:
    print(rim[a])
else:
    print('ошибка')

#Задача на YES or NO

a = int(input())
if a % 2 != 0:
    print('YES')
elif a % 2 == 0 and 2 <= a <= 5:
    print('NO')
elif a % 2 == 0 and 6 <= a <= 20:
    print('YES')
elif a % 2 == 0 and a > 20:
    print('NO')


a = int(input())
if a % 2 != 0:
    print('YES')
elif 2 <= a <= 5:   
    print('NO')
elif 6 <= a <= 20:  
    print('YES')
else:             
    print('NO')

#Задача про ход слона

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (x1 - x2) == (y1 - y2) or  (x1 - x2) == -(y1 - y2):
    print('YES')
else:
    print('NO')

#Задача про ход коня

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
dx = x1 - x2
dy = y1 - y2
if dx == 2 and dy == 1:
    print('YES')
elif dx == 2 and dy == -1:
    print('YES')
elif dx == -2 and dy == 1:
    print('YES')
elif dx == -2 and dy == -1:
    print('YES')
elif dx == 1 and dy == 2:
    print('YES')
elif dx == 1 and dy == -2:
    print('YES')
elif dx == -1 and dy == 2:
    print('YES')
elif dx == -1 and dy == -2:
    print('YES')
else:
    print('NO')

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
dx = abs(x1 - x2)
dy = abs(y1 - y2)
if (dx == 2 and dy == 1) or (dx == 1 and dy == 2):
    print('YES')
else:
    print('NO')

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if abs(x1 - x2) * abs(y1 - y2) == 2:
    print('YES')
else:
    print('NO')

#Задача про ход Ферзя

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (x1 - x2) == (y1 - y2) or  (x1 - x2) == -(y1 - y2):
    print('YES')
elif x1 == x2 or y1 == y2:
    print('YES')
else:
    print('NO')


x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
диаг = abs(x1 - x2) == abs(y1-y2)
верт = x1 == x2 or y1 == y2
if диаг or верт:
    print('YES')
else:
    print('NO')
