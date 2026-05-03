
#Only even numbers. Ищем только четные цифры

yes = 0
for i in range(10):
    num = int(input())
    if num % 2 == 0:
        yes += 1
if yes == 10:
    print('YES')
else:
    print('NO')

# #Через флаги

flag = 'YES'
for _ in range(10):
    n = int(input())
    if n % 2 == 1:
        flag = 'NO'
print(flag)

# #Через массив и функцию all

numbers = [int(input()) for _ in range(10)]
if all(num % 2 == 0 for num in numbers):
    print("YES")
else:
    print("NO")

#Знакочередующаяся сумма

n = int(input())
total = 0
for i in range(1, n + 1):
    total += ((-1)**(i+1)) * i
print(total)

# #
n = int(input())
total = 0
for i in range(1, n + 1):
    if i % 2 == 1:
        total += i
    else:
        total -= i
print(total)

# #*

n = int(input())
# Используем свойство: для нечётного n → (n+1)//2, для чётного → -n//2
print((n + 1) // 2 if n & 1 else -n // 2)


#Наибольшие числа 

a = int(input())
max1 = 0
max2 = 0
for _ in range(a):
    n = int(input())
    if n > max1:
        max2 = max1
        max1 = n
    elif n > max2  and n != max1:
        max2 = n
print(max1, max2, sep='\n')

#Через сортировку 

n = int(input())
s = []
for i in range(n):
    a = int(input())
    s.append(a)
s.sort()
print(s[-1])
print(s[-2])
#
n = int(input())
res = []
for i in range(1, n+1):
    num = int(input())
    res.append(num)
res = sorted(res)
print(res[-1], res[-2], sep='\n')

# #Через замену переменных
n = int(input())
b = -1
a = 0
for i in range(n):
    k = int(input())
    if k > b:
        b, a = k, b
    elif k < b:
        if k > a:
            a = k
print(b)
print(a)

#Последовательность Фибоначчи

n = int(input())
a, b = 1, 1
for i in range(n):
    print(a, end=' ')
    a, b = b, a + b
