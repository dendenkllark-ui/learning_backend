


# # Проверить является ли введеный ip адресс корректным

# s = input()
# flag = True
# w = s.split('.')
# for n in w:
#     if n.isdigit():
#         if 0 <= int(n) <= 255:
#          flag = True
#     else:
#         flag = False
#         break
# if flag:
#     print('ДА')
# else:
#     print('НЕТ')

# # 
# s = input().split(".")
# for n in s:
#     if not (0 <= int(n) <= 255):
#         print("НЕТ")
#         break
# else:
#     print("ДА")

# # Добавить конкретный разделитель в строку

# s = input()
# d = list(s)
# a = input()
# print(a.join(s))

# #
# s = input()
# separator = input()
# res = separator.join(s)
# print(res)


# #### Объединить цифры в строке по парам

# s = input()  # Ввод: 121525
# words = []
# # Бежим по строке с шагом 2 (0, 2, 4...)
# for i in range(0, len(s), 2):
#     # Берем кусочек от текущего индекса до текущего + 2
#     words.append(s[i:i+2])
# print(words)  # На выходе: ['12', '15', '25']


# Посчитать сколько в строке одинаковых пар 

s = input().split()
total = 0
c = []
for n in s:
    if n not in c:
        k = s.count(n)
        pairs = (k * (k - 1)) // 2
        total += pairs
        c.append(n)
print(total)


# через set

s = input().split()
total_pairs = 0
# Перебираем только уникальные числа
for num in set(s):
    n = s.count(num)            # Считаем, сколько раз число встретилось
    total_pairs += (n * (n - 1)) // 2  # Считаем все математические пары
print(total_pairs)


# Алгорит поиска пар 
num, count = input().split(), 0
for i in range(len(num)):
    for j in range(i + 1, len(num)):
        if num[i] == num[j]:
            count += 1
print(count)
        
