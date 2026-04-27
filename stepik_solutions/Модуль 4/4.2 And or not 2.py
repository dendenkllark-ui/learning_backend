num = int(input())
if 1000 <= num <= 9999 and (num % 7 == 0 or num % 17 == 0):
    print('YES')
else:
    print('NO')

a = int(input())
b = int(input())
c = int(input())
if (a + b > c) and (a +c > b) and (b +c > a):
    print('YES')   
else:
    print('NO')

# Задача про високосный год

a = int(input())
if a % 4 == 0 and not a % 100 == 0 or a % 400 == 0:
    print('YES')
else:
    print('NO') 

# Задача про ладью

x1 = int(input())
y1 = int(input())
x2 = int(input())  
y2 = int(input())
if x1 == x2 or y1 == y2:
    print('YES')   
else:
    print('NO')

# Задача про ладью

a, b, a1, b1 = int(input()), int(input()), int(input()), int(input())
if 1 <= a <= 8 and 1 <= b <= 8 and 1 <= a1 <= 8 and 1 <= b1 <= 8:
    if a == a1 or b == b1:
        print('YES')
    elif a == a1 and b == b1:
        print('NO')
    else:
        print('NO')

# Задача про короля

x1 = int(input())
y1 = int(input())
x2 = int(input())  
y2 = int(input())
if 1 <= x1 <= 8 and 1 <= y1 <= 8 and 1 <= x2 <= 8 and 1 <= y2 <= 8:
    dx = x1 - x2
    dy = y1 - y2
if (dx ==1 or dx == -1 or dx == 0) and (dy == 1 or dy == -1 or dy == 0):
    if dx == 0 and dy == 0:
        print('NO')
    else:
        print('YES')
else:
    print('NO')

# Задача про короля

x1 = int(input())
y1 = int(input())
x2 = int(input())  
y2 = int(input())
dx = x1 - x2
dy = y1 - y2
if -1 <= dx <= 1 and -1 <= dy <= 1:
    if dx == 0 and dy == 0:
        print('NO')
    else:
        print('YES')
else:
    print('NO')