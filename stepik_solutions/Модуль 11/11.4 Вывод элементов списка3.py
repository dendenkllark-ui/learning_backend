

# Удалить из списка самое большое и самое маленькое число

n = int(input())
s = []
for i in range(n):
    s.append(int(input()))
s.remove(max(s))
s.remove(min(s))
print(*s, sep='\n')

#
n = int(input())
numbers = []
for _ in range(n):
    numbers.append(int(input()))
maximum = numbers.index(max(numbers))
del numbers[maximum]
minimum = numbers.index(min(numbers))
del numbers[minimum]
print(*numbers, sep = '\n')


# Входит ли какой-то элемент списка в другой список

n = int(input())
s = []
for i in range(n):
    x = input()
    s.append(x)
word = input().lower()
for k in s:
    if word in k.lower():
        print(k)


# Вхлодит ли все элементы поиска в какую-либо строку списка

n = int(input())
s = []
for i in range(n):
    x = input()
    s.append(x)   
word = []
m = int(input())
for j in range(m):
    word.append(input().lower())

for k in s:
    flag = True
    for w in word:
        if w not in k.lower():
            flag = False
            break
    if flag:
        print(k)

