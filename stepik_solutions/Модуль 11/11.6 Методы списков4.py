

# Добавить строку в список из чисел
# Отсортировать список чисел от меньшего к большему и от большего к меньшему, 

s = input().split()
n = []
for i in s:
    n.append(int(i))

n.sort()
print(*n)
n.sort(reverse=True)
print(*n)

#
sp = [int(i) for i in input().split()]
sp.sort()
print(*sp)
sp.sort(reverse = True)
print(*sp)

# Отсортировать список строк в алфавитном порядке

n = int(input())
s = []
for i in range(n):
    s.append(input())
s.sort()
print(*s, sep='\n')