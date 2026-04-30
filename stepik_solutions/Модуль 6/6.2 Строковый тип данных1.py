#Соединение строк

s1 = '"Python is a great language!", said Fred.' + ' "I don\'t ever remember having this much fun before."'
print(s1)

#What's Your Name?

a = input()
b = input()
print('Hello'+ ' ' + a + ' ' + b + '!', 'You have just delved into Python')

#Футбольшая команда

a = input()
print('Футбольная команда', a, 'имеет длину', len(a), 'символов')

#Три города

a = input()
b = input()
c = input()
if min(len(a), len(b), len(c)) == len(a):
    print(a)
if min(len(a), len(b), len(c)) == len(b):
    print(b)
if min(len(a), len(b), len(c)) == len(c):
    print(c)
if max(len(a), len(b), len(c)) == len(a):
    print(a)
if max(len(a), len(b), len(c)) == len(b):
    print(b)
if max(len(a), len(b), len(c)) == len(c):
    print(c)

city = [input(), input(), input()]
city.sort(key=len)
print(city[0])
print(city[-1])

city = [input(), input(), input()]
shortest = min(a, b, c, key=len)
longest = max(a, b, c, key=len)
print(shortest, longest, sep='\n')

#Арифметические строки

a = len(input())
b = len(input())
c = len(input())
mid = [a, b, c]
if (min(mid) + max(mid)) == ((sum(mid) - max(mid) - min(mid)) * 2):
    print('YES')
else:
    print('NO')




