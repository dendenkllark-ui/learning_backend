

# Вывести сумму квадратов элементов списка
n = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
sum = 0
for i in n:
    sum += i**2
print(sum)

# Вывести из n чисел сначала отрицательные, потом нули и потом положительные

n = int(input())
a =[] 
b = []
c = []
for i in range(n):
    s = int(input())
    if s < 0:
        a.append(s)
    elif s == 0:
        b.append(s)
    else:
        c.append(s)
m = a + b + c
print(*m, sep ='\n')    # for i in res: \print(i)


# Вывести только уникальные n строк

n = int(input())
a = []
for i in range(n):
    s = input()
    if s not in a:
        a.append(s)
print(*a, sep ='\n')


# Вывести решение уравнений для каждого введенного X и вывести на отльной строке

n = int(input())
a = []
y = []
for i in range(n):
    x = (int(input()))
    y.append(x)
    s = x**2 + 2*x + 1
    a.append(s)
print(*y, sep='\n')
print()
print(*a, sep='\n')

#
n = int(input())
start = [int(input()) for _ in range(n)]
print(*start, sep='\n')
print()
end = [i**2+2*i+1 for i in start]
print(*end, sep='\n')

#
n = int(input())
seq = []
for _ in range(n):
    seq.append(int(input()))
func_seq = []
for el in seq:
    func_seq.append(el ** 2 + 2 * el + 1)
print(*seq, sep="\n")
print()
print(*func_seq, sep="\n")
