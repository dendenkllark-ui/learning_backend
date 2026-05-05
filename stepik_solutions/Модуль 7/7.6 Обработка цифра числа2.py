#Вывести число в обратном порядке в столбик
num = int(input())  
while num != 0:
    n = num % 10
    num = num // 10
    print(n)

##
for digit in reversed(input()):
    print(digit)

#Вывести число в обратном порядке в стрчоку
num = int(input())  
while num != 0:
    n = num % 10
    num = num // 10
    print(n, end='')

##
print(int(input()[::-1]))
#
print(*reversed(input()), sep='')


#max и min

#через while
n = int(input())
max_digit = 0
min_digit = 9

while n > 0:
    cur_digit = n % 10
    
    max_digit = max(max_digit, cur_digit)
    min_digit = min(min_digit, cur_digit)
    
    n //= 10
    
print("Максимальная цифра равна", max_digit)
print("Минимальная цифра равна", min_digit)

#через строку
num = input()
m = min(num)
n = max(num)
print(f'Максимальная цифра равна {n}\nМинимальная цифра равна {m}')

#Все вместе

num = input()
l = len(num)
s = 0
b = 1
for i in num:
    s += int(i)
    b *= int(i)
print(s, l, b, s / l, sep='\n')
num = int(num)
for i in range(1, l + 1):
    x = num // 10 ** (l - i) % 10
    if i == 1:
        first = x
    if i == l:
        last = x
        print(first, first + last, sep='\n')

#через while
n = int(input())

digit_sum = 0
digit_cnt = 0
digit_product = 1
last_digit = n % 10

while n > 0:
    cur_digit = n % 10

    first_digit = cur_digit
    digit_sum += cur_digit
    digit_cnt += 1
    digit_product *= cur_digit
    
    n //= 10

digit_average = digit_sum / digit_cnt
first_last_sum = first_digit + last_digit

print(digit_sum)
print(digit_cnt)
print(digit_product)
print(digit_average)
print(first_digit)
print(first_last_sum)



