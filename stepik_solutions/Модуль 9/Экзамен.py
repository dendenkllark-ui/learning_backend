# #
# s = 'Python rocks!'
# print(len(s))

# #
# s = 'Python rocks!'
# print(s[3])

# #
# s = 'Python rocks!'
# print(s[1:6])

# #
# s = '###Python rocks!####'
# print(s.strip('#'))

# #
# s = 'Python rocks!'
# print(s.upper())

# #
# s = 'Python rocks!'
# print(s.replace('o', '@'))


# # Удалить из строки символы кратные 3

# n = input()
# new = ''
# for i in range(0, len(n)):
#     if i % 3 != 0:
#         new += n[i]
# print(new)


# #  Заменить в строке все цифры 1 на one
# n = input()
# print(n.replace('1', 'one'))

# # Удалить все символы @ встроке
# n = input()
# print(n.replace('@', ''))

# # Вывести индекс второго вхождения буквы f в строке. Если буква f встречается только один раз, то вывести число -1, 
# # а если не встречается ни разу, то вывести число -2.
# s = input()
# if s.count('f') == 1:
#     print(-1)
# elif s.count('f') == 0:
#     print(-2)
# else:
#     first = s.find('f')
#     second = s.find('f', first + 1)
#     print(second)

# Перевернуть строку между двумя одинаковыми символами
s = input()
a = s.find('h')
b = s.rfind('h')
x = s[a+1:b][::-1]  # так мы переворачиваем строку между символами h, без самих символов. 
s = s[:a] + x + s[b+1:]   # Если нужно перевренуть и сами, то диапазон будет s[a:b+1][::-1]
print(s)