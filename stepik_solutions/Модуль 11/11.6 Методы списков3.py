

# Все и сразу

n = [8, 9, 10, 11]
n[1] = 17
n.extend([4, 5, 6])
n.pop(0)    # del n[0]
n = n * 2
n.insert(3, 25)
print(n)


# Удалить из строки все комментарии - всё что начинается с #

n = int(input().strip('# '))
for i in range(n):
    s = input()
    if '#' in s:
        s = s.split('#')[0]
    m = s.rstrip()
    print(m)

#
# считаем кол-во строк в программе
n = int(input()[1:])
for _ in range(n):
    # принимаем текущую строку
    s = input()
    # ищем символ # в строке
    hash_index = s.find("#")
    # если нашли символ # в строке
    if hash_index != -1:
        # присваиваем для s новую строку,
        # где убираем # и всё, что после #
        s = s[:hash_index]
    # убираем пробелы справа
    s = s.rstrip()
    print(s)
    

#
n = input()
for _ in range(int(n[1:])):
    s = input()
    if '#' in s:
        s = s[:s.find('#')]
    print(s.rstrip())

# Переставить местами мин и макс

n = [int(x) for x in input().split()]
a = min(n)
b = max(n)
min = n.index(a)
max = n.index(b)
n[min], n[max] = n[max], n[min]
print(' '.join([str(x) for x in n]))

#
seq = []
for el in input().split():
    seq.append(int(el))
mx_ind = seq.index(max(seq))
mn_ind = seq.index(min(seq))
seq[mx_ind], seq[mn_ind] = seq[mn_ind], seq[mx_ind]
print(*seq)
