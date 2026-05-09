#Вывести текст, если в строке есть цифра
a = input()
s = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
n = 0
for c in a:
    if c in s:
        n += 1
if n > 0:
    print('Цифра')
else:
    print('Цифр нет')

#
s = input()
digits = '0123456789'
for c in s:
    if c in digits:
        print('Цифра')
        break
else:
    print('Цифр нет')
    
#Через флаг
n=input()
flag=False
for i in range(10):
    if str(i) in n:
        flag=True
if flag==True:
    print('Цифра')
else:   
     print('Цифр нет')
     
#
n=input()
a = 0
b = 0
s = '*'
m = '+'
for c in n:
    if c in m:
        a += 1
    if c in s:
        b += 1
print(f'Символ + встречается {a} раз\nСимвол * встречается {b} раз')

#
s = input()
cnt_plus = 0
cnt_mul = 0
for el in s:
    if el == "+":
        cnt_plus += 1
    elif el == "*":
        cnt_mul += 1
print("Символ + встречается", cnt_plus, "раз")
print("Символ * встречается", cnt_mul, "раз")




