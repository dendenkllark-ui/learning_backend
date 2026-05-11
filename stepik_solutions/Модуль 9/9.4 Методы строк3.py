# #Чем оканчивается строка

# s = input()
# if s.endswith('.com') or s.endswith('.ru'):    #Можео объединить if text.endswith(('.ru', '.com'))
#     print('YES')
# else:
#     print('NO')

# ##
# text = input()
# print('YES' if text.endswith('.com') or text.endswith('.ru') else 'NO')

# #Самый частотный символ в строке

# s = input()
# max = 0
# best = 0
# for i in range(len(s)):
#     n = s.count(s[i])
#     if n >= max:
#         max = n
#         best = s[i]
# print(best)

# ##
# s = input()
# most_common = s[0]
# for el in s:
#     if s.count(el) >= s.count(most_common):
#         most_common = el
        
# print(most_common)

# #Первое и последнее вхождение

# s = input()
# if s.count('f') == 1:
#     print(s.find('f'))
# if s.count('f') > 1:
#     print(s.find('f'), s.rfind('f'))
# if s.count('f') == 0:
#     print('NO')

# ##
# s = input()
# if 'f' in s:
#     if s.count('f')==1:
#         for i in range(len(s)):
#             if s[i]=='f':
#                 print(i)
#     elif s.count('f')>=2:
#         print(s.find('f'), s.rfind('f'))
# else:
#     print('NO')

## Удаление фрагмента строки

s = input()
a = s.find('h') 
b = s.rfind('h')
print (s[:a] + s[b+1:])

#
s = input()
s = s.replace(s[s.find("h"):s.rfind("h") + 1], "")
print(s)