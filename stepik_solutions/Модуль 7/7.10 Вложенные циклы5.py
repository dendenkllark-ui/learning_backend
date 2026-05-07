
# #Ищем сколько делителей есть у числла
# n = int(input())
# for i in range(1, n + 1):
#     count = 0
#     for j in range(1, i + 1):
#         if i % j == 0:
#             count += 1
#     print(i, "+" * count, sep="")

# #Численный треугольник 2


# n = int(input())
# count = 1
# for i in range(1, n + 1):
#         for j in range (1, i + 1):
#             print(count,  end=' ')
#             count += 1
#         print()

# #решение через сумму наименьшего и наибольшего числа
# n = int(input())
# largest = 0
# smallest = 1
# for i in range(1, n + 1):
#     for j in range(i):
#         num = smallest + largest
#         if num > largest:
#             largest = num
#         print(num, end=" ")
#     print()


#Простые числа 👌 (Найти все простые числа от a до b)
#через else
# a = int(input())
# b = int(input())
# for i in range (a, b):
#     if i < 2:
#         continue
 
#     for j in range (2, i):
#         if i % j == 0:
#             break
#     else:
#         print(i)
# #через флаг
# a = int(input())
# b = int(input())
# for i in range(a, b + 1):
#     if i < 2:
#         continue
#     flag = True 
#     for j in range(2, int(i**0.5) + 1):
#         if i % j == 0:
#             flag = False  
#             break             
#     if flag:
#         print(i)
# ##
# a, b = int(input()), int(input())
# for num in range(a, b + 1):
#     if num == 1:
#         continue
#     for i in range(2, num):
#         if num % i == 0:
#             break
#     else:
#         print(num)

#Сумма факториалов
from math import factorial
n = int(input())
sum = 0
for i in range (1, n +1 ):
    sum += factorial(i)
print(sum)
#
n = int(input())
total = 0
for i in range(1, n + 1):
    factorial = 1
    for j in range(1, i + 1):
        factorial *= j
    total += factorial
print(total)