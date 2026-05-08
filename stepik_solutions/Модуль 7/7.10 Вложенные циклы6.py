
# Решение уравнениия  x + 3*y + 2*z = m

for x in range(1, 11):
    for y in range(1, 21):
        for z in range(1, 201):
            if x * 10 + y * 5 + z * 0.5 == 100:
                if x + y + z == 100:
                    total += 1
                    print('x =', x, 'y =', y, 'z =', z)
print('Общее количество натуральных решений =', total)


n = int(input())
m = int(input())
c = 0
for x in range(1, n):
    for y in range(1, n):
        for z in range(1, n):
            if x + y * 3 + z * 2 == m:
                c += 1
                print(f'{x} + 3x{y} + 2x{z} = {m}')
if c == 0:
    print('При заданных n и m решений не существует.')
    
##
n, m = int(input()), int(input())
cnt = 0
for j in range(1, n):
    for k in range(1, n):
        for i in range(1, n):
            if i + 3*j + 2*k == m:
                cnt += 1
                print(i, ' + 3×', j, ' + 2×', k, ' = ', m, sep='')
                
if cnt == 0:
    print('При заданных n и m решений не существует.')

# Делители (Больший делитесь и сумма делителей)
a = int(input())
b = int(input())
n = 0
m = 0
for i in range (a, b + 1):
    sum = 0
    for j in range(1, i + 1):
        if i % j == 0:
            sum += j
    if sum >= m:
        m = sum
        n = i
print(n, m)