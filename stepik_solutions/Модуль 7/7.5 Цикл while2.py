# Количество пятёрок 5️⃣

num = int(input())
sum = 0
while 1 <= num <= 5:
    if num == 5:
        sum += 1
    num = int(input())
print(sum)

sum = 0
while True:
    num = int(input())
    if not (1 <= num <= 5):
        break
    if num == 5:
        sum += 1
print(sum)

#Первый никнейм 👉

while True:
    a = input()
    if '_' not in a:
        break
print(a)

#
text = input()
while text != 'СТОП':
    if '_' not in text:
        print(text)
    text = input()
#
name = input()
while '_' in name:
    name = input()
print(name)

#Сколько ждать? ⏱️

name = input()
time = -1
while name != "Левон":
    time += 1
    name = input()
    if name == "Александра":
        time = -1
print(time)

#
q = input()
w = 0
while q != 'Александра':
    q = input()    
while q != 'Левон':
    w += 1
    q = input()
print(w - 1)

#Ведьмаку заплатите чеканной монетой 
count = 0
n = int(input())
while n >= 25:
    n -= 25
    count += 1
while n >= 10:
    n -= 10
    count += 1
while n >= 5:
    n -= 5
    count += 1
while n >= 1:    #Можно просто написать coutn = count + n (count += nrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr)
    n -= 1
    count += 1
print(count)

#без while
n = int(input())
count = n // 25
n %= 25
count += n // 10
n %= 10
count += n // 5
n %= 5
count += n //1
print(count)

#Временной промежуток ⏱️

h1, m1, h2, m2 = int(input()), int(input()), int(input()), int(input()) 
print(f'{h1:02}:{m1:02}')
while h1 != h2 or m1 != m2:
    m1 += 1
    if m1 == 60:
        m1 = 0
        h1 += 1
    if h1 == 24:
        h1 = 0
    print(f'{h1:02}:{m1:02}')

#
h1, m1, h2, m2 = int(input()), int(input()), int(input()), int(input()) 
print('{:02}:{:02}'.format(h1, m1))
while h1 != h2 or m1 != m2:
    m1 += 1
    if m1 == 60:
        m1 = 0
        h1 += 1
    if h1 == 24:
        h1 = 0
    print('{:02}:{:02}'.format(h1, m1))

##
h1, m1, h2, m2 = int(input()), int(input()), int(input()), int(input()) 
print(str(h1).zfill(2), str(m1).zfill(2), sep=':')
while h1 != h2 or m1 != m2:
    m1 += 1
    if m1 == 60:
        m1 = 0
        h1 += 1
    if h1 == 24:
        h1 = 0
    print(str(h1).zfill(2), str(m1).zfill(2), sep=':')


###
h1, m1 = int(input()), int(input())
h2, m2 = int(input()), int(input())
while h1 < h2 or (h1 == h2 and m1 <= m2):   
    if h1 < 10:
        h = '0' + str(h1)
    else:
        h = str(h1)
    if m1 < 10:
        m = '0' + str(m1)
    else:
        m = str(m1)
        
    print(h, m, sep=':')
    
    m1 += 1
    if m1 == 60:
        h1 += 1
        m1 = 0