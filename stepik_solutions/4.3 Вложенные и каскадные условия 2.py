#Задача про самописный калькулятор

# a = int(input())
# b = int(input())  
# c = input()
# if c == '+':
#     print(a + b)
# elif c == '-':
#     print(a - b)   
# elif c == '*':
#     print(a * b)
# elif c == '/':
#     if b != 0:
#         print(a / b)
#     else:
#         print('На ноль делить нельзя!')
# else:
#     print('Неверная операция')

#Задача про цветовой микшер

# a = input()
# b = input()
# if (a == 'красный' and b == 'синий') or (a == 'синий' and b == 'красный'):
#     print('фиолетовый')
# elif ( a == 'красный' and b == 'желтый') or (a == 'желтый' and b == 'красный'):
#     print('оранжевый')
# elif (a == 'синий' and b == 'желтый') or (a == 'желтый' and b == 'синий'):
#     print('зеленый')
# elif a == b and (a == 'красный' or a == 'синий' or a == 'желтый'):
#     print(a)
# else:
#     print('ошибка цвета')

#Задача про цвета колеса рулетки

# a = int(input())
# if a == 0:
#     print('зеленый')
# elif 1 <= a <= 10 or 19 <= a <= 28:
#     if a % 2 == 0:
#         print('черный')
#     else:
#         print('красный')
# elif 11 <= a <= 18 or 29 <= a <= 36:
#     if a % 2 == 0:
#         print('красный')
#     else:        
#         print('черный')
# else:
#     print('ошибка ввода')

#Задача про пересечение отрезков

a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
if b1 < a2 or b2 < a1:
    print('пустое множество')
elif b1 == a2:
    print(b1)
elif b2 == a1:
    print(a1)
else:
    if a1> a2:
        x = a1
    else:
        x = a2
    if b1 < b2:
        y = b1
    else:
        y = b2
    print(x, y)

a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input()) 
if a2 < a1:
    a1, b1, a2, b2 = a2, b2, a1, b1 
if a2 > b1: 
    print("пустое множество")
elif a2 == b1:
    print(a2)
else:
    if b1 < b2:
        print(a2, b1)
    else:
        print(a2, b2)

a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input()) 
if min(b1, b2) < max(a1, a2): 
    print('пустое множество')
elif min(b1, b2) == max(a1, a2):
    print(min(b1, b2))
else:
    print(max(a1, a2), min(b1, b2))