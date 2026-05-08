


# # #Рисуем таблицу из *
# # n = int(input())
# # for i in range(1, n + 1):
# #     if i == 1 or i == n:
# #         print('*' * 19)
# #     else:
# #         print(f"*{17 * ' '}*")

# # #через вложенные циклы
# # n = int(input())
# # w = 19
# # for i in range(1, n + 1):
# #     for j in range(1, w + 1):
# #         if i == 1 or i == n or j == 1 or j == w:
# #             print("*", end='')
# #         else:
# #             print(" ", end='')
# #     print()

# # #
# # n = int(input())

# # for i in range(n):
# #     if i == 0 or i == n - 1:
# #         cur_sep = "*"
# #     else:
# #         cur_sep = " "
        
# #     print("*", "*", sep=cur_sep * 17)


# #Третья цифра 3️⃣
# n = int(input())
# count = 0
# num = n
# while num > 0:
#     num //= 10
#     count +=  1
# while count > 3:
#     n //= 10
#     count -= 1
# s = n % 10
# print(s)

# #
# n = int(input())
# while n > 999:
#     n //= 10
# print(n % 10)

# # можно просто сразу вывести только первые 3 цифры потом отпбросить последнюю
# n = int(input())
# d = len(str(n))
# # Делим n на 10^(d-3), затем берём остаток от деления на 10
# print(n // 10 ** (d - 3) % 10) 


# #Все вместе 2
# num = int(input())
# sum3 = 0
# last = num % 10
# x = 0
# count_2 = 0
# sum5 = 0
# res7 = 1
# sum05 = 0

# while num > 0:
#     n = num % 10
#     if n == 3:
#         sum3 += 1
#     if n == last:
#         x += 1
#     if n % 2 == 0:
#         count_2 += 1
#     if n > 5:
#         sum5 += n
#     if n > 7:
#         res7 *= n
#     if n == 0 or n == 5:
#         sum05 += 1
#     num //= 10
# print(sum3, x, count_2, sum5, res7, sum05, sep='\n')

#Числа Рамануджана 🌶️
n = int(input())
res = []
for a in range(1, n):
    for b in range(a + 1, n):       
        for c in range(a + 1, n):   
            for d in range(c + 1, n): 
                if a**3 + b**3 == c**3 + d**3:
                    s =  a**3 + b**3
                    res.append(s)
res.sort()
for s in res:
    print(s)

# #Через список
# limit = 50000  # Диапазон поиска
# sums = {}      # Словарь: {сумма_кубов: [список пар чисел]}

# # Перебираем числа a и b
# for a in range(1, 40): # Числа небольшие, так как кубы быстро растут
#     for b in range(a + 1, 40):
#         s = a**3 + b**3
        
#         if s in sums:
#             # Если такая сумма уже встречалась — мы нашли число Рамануджана!
#             prev_a, prev_b = sums[s]
#             print(f"Число Рамануджана: {s} ({prev_a}^3 + {prev_b}^3 и {a}^3 + {b}^3)")
#         else:
#             sums[s] = (a, b)       




