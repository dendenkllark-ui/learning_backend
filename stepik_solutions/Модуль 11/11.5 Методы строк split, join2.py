

# Вывести строку по словам в столбик

s = input()
words = s.split()
print(*words, sep='\n')

# Вывести инициалы из полученных на входе ФИО

s = input()
words = s.split()
ФИО = ''
for i in range(len(words)):
    ФИО += words[i][0] + '.'
print(ФИО)

#
s = input()
words = s.split()
ФИО = ''
for word in words:
    ФИО += word[0] + '.'
print(ФИО)

#
name_initials = []
for s in input().split():
    name_initials.append(s[0])
formatted_name = '.'.join(name_initials) + '.'
print(formatted_name)

#
full_name = input().split()
print(full_name[0][0], full_name[1][0], full_name[2][0], sep=".", end=".")

# Разобрать путь к папке на отдельные каталоки

s = input().split('\\')
print(*s, sep='\n')


# Построить столбчатую диаграмму по заданной последовательности чисел

s = input().split()
a = []
for i in range(len(s)):
    a.append('+'*int(s[i]))
print(*a, sep='\n')

#
s = input().split()
for i in range(len(s)):
    print(int(s[i]) * '+')

#
seq = input().split()
for el in seq:
    print("+" * int(el))
    
