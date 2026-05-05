#Вторая цифра
num = int(input())
n = len(str(num))
for i in range(1, 3):
    x = num // 10 ** (n - i) % 10
print(x)

# через while
n = int(input())
while n > 99:
    n //= 10

second_digit = n % 10
print(second_digit)

#Одинаковые цифры
num = input()
n = len(num)
flag = 'YES'
for i in range (1, n):
    x = num[i]
    y = num[i - 1]
    if x != y:
        flag = 'NO'
        break
print(flag)

#Через while
n = int(input())
flag = "YES"
last_digit = n % 10
while n > 0:
    cur_digit = n % 10
    
    if last_digit != cur_digit:
        flag = "NO"

    n //= 10

print(flag)


# Упорядоченные цифры 🌶️ справа на лево большие к меньшим

n = int(input())
flag = "YES"
last_digit = n % 10
while n > 0:
    cur_digit = n % 10
    if last_digit > cur_digit:
        flag = "NO"
        break
    last_digit = cur_digit
    n //= 10
print(flag)

#
n = int(input())
flag = "YES"
last_digit = n % 10
while n > 0:
    if last_digit > n % 10:
          flag = "NO"
    last_digit = n % 10
    n //= 10
print(flag)

#Четные цифры 2️⃣🌶️

num = int(input())
n = len(str(num))
s = 0
for i in range(1, n + 1):
    digit = num // 10 ** (n - i) % 10
    if digit % 2 == 0:
        s += 1
        print(s, '-я', ' четная цифра равна ', digit, sep='')
if s == 0:
    print('Четных цифр в числе нет')
