# #Постчитать по формуле цифры когда из набора слов

# a = input()
# b = input()
# c = input()
# d = input()
# x = max(a, b, c, d)
# y = min(a, b, c, d)
# z = (ord(x[-1])*ord(y[-1]))**2
# print(z)

# # Строковый мин и макс

# n = input()
# x = n
# y = n
# while n != "КОНЕЦ":
#     if n > x:
#         x = n
#     if n < y:
#         y = n
#     n = input()
# print("Минимальная строка ⬇️:", y)
# print("Максимальная строка ⬆️:", x)


# # Сравнить строки без цифр и символов не учитывая их регистр

# a = input().lower()
# b = input().lower()
# x1 = ''
# x2 = ''
# for i in a:
#     if i.isalpha():
#         x1 += i
# for i in b:
#     if i.isalpha():
#         x2 += i
# if x1 == x2:
#     print('YES')
# else:
#     print('NO')

# Сортировка строк по порядку

a = input()
b = input()
c = input()
x = max(a, b, c)
y = min(a, b, c)
if a != x and a != y:
    mid = a
elif b != x and b != y:
    mid = b
else:
    mid = c
print(y, mid, x)

# 
a = input()
b = input()
c = input()

# Создаем из них список
strings = [a, b, c]

# Находим максимум и минимум встроенными функциями Python
maximum = max(strings)
minimum = min(strings)

# Удаляем максимум и минимум из списка
strings.remove(maximum)
strings.remove(minimum)

# В списке остался ровно один элемент — тот, что посередине
middle = strings[0]

print("Минимум:", minimum)
print("Средняя строка:", middle)
print("Максимум:", maximum)

# Через сортировку

a = input()
b = input()
c = input()
l = [a, b, c]
l.sort()
print(*l)

