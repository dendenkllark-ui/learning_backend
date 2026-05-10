# # Проверить начинается ли ФИО с заглавных букв

# n = input()
# if n == n.title():
#     print('YES')
# else:
#     print('NO')


# #Поменять все регистры наоборт

# s = input()
# print(s.swapcase())

# #Проверить есть ли слово в строке во всемозможных регистрах

# s = input()
# n = 'хорош'
# n = n.lower()
# if n in s.lower():
#     print('YES')
# else:
#     print('NO')

# #
# s = input().lower()  # Сразу делаем всю строку строчной
# if 'хорош' in s:
#     print('YES')
# else:
#     print('NO')

#Посчитать сколько нижних символов в строке

s = input()
n = len(s)
count = 0
for i in range(n):
    if s[i] == s[i].lower() and s[i].isalpha():    # Проверке является ли символ числом или буквой
        count += 1
print(count)

#
s = input()
count = 0
for a in s:
    if 'a' <= a <= 'z':
        count += 1
print(count)

#####
s = input()
count = 0
for i in s:
    if i.islower():
        count += 1
print(count)

##
s = input()
count = 0
for i in s:
    if i != i.upper():
        count += 1
print(count)

##
s = input()
letters = "abcdefghijklmnopqrstuvwxyz"
cnt_al_lower = 0
for el in s:
    if el in letters:
        cnt_al_lower += 1
        
print(cnt_al_lower)