#Задача про скорости Зума и Флеша

a = int(input())
b = int(input())
if a > b:
    print('NO')
elif a < b:
    print('YES')
else:
    print("Don't know")

#Задача про вид треугольника

a, b, c = int(input()), int(input()), int(input())
if a == b == c:
    print('Равносторонний')
elif a == b or a == c or b == c:
    print('Равнобедренный')
else:
    print('Разносторонний')

#Задача про серединное число

a, b, c = int(input()), int(input()), int(input())
if (a > b > c) or (c > b > a):
    print(b)
elif (b > a > c) or (c > a > b):
    print(a)
else:
    print(c)

#Задача про количесто дней

a = int(input())
if a == 2:
    print(28)
elif a == 4 or a == 6 or a == 9 or a == 11:
    print(30)
else:
    print(31)

a = int(input())
if a in (1, 3, 5, 7, 8, 10, 12):
    print(31)
elif a in (4, 6, 9 , 11):
    print(30) 
if a == 2:
    print(28)

a = int(input())
if a == 2:
    print(28)
elif a in (4, 6, 9 , 11):
    print(30) 
else:
    print(31)  
# 
# Задача про церемонию взвешивания

a = int(input())
if a < 60:
    print('Легкий вес')
elif a < 64:
    print('Первый полусредний вес')
elif a < 69:
    print('Полусредний вес')

a = int(input())
if a < 69:
    if a < 64:
        if a < 60:
            print('Легкий вес')
        else:
            print('Первый полусредний вес')
    else:
        print('Полусредний вес')