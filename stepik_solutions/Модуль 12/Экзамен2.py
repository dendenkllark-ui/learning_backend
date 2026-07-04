# Сумма двух списков

L = input().split()
M = input().split()
x = []
for i in range(len(L)):
    a = int(L[i]) + int(M[i])
    x.append(a)
print(*x)

#Методом списочного выражения
L = input().split()
M = input().split()
print(*[int(L[i]) + int(M[i]) for i in range(len(L))])



# Сумма чисел

a = input().split()
s = '+'.join(a)
print(f'{s}={sum([int(i) for i in a])}')


# Найти длинну самого длинного слова

a = input().split()
m = ''
for w in a:
    if len(w) > len(m):
        m = w
print(len(m))

# В одну строчку 
print(max([len(i) for i in input().split()]))


# Переписать текст на шифр

print(*[a[1:] + a[0] + 'ки' for a in input().split()])
#
print(' '.join([w[1:] + w[0] for w in input().split()]))



