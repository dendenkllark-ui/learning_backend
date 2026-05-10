# Вывести конкретный символ в строке
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
for i in range(7, 8):
    print(s[7])
#
s = "two In 2010, someone paid 10k Bitcoin for  pizzas."
print(s[1])

#Вывести текст в столбик
s = input()
for i in range(0, len(s), 2):
    print(s[i])

# Вывести текст задом наперед в столбик
s = input()
for i in range(-1, -len(s)-1, -1):
    print(s[i])

# Вывести ФИО человека
a = input()
b = input()
c = input()
print(b[0]+a[0]+c[0])

#Вывести текст и номер по очереди

a = input() 
for i in range(1, len(a) + 1):
    print(str(i) + ')', a[i-1])
#
a = input() 
for i in range(len(a)):
    print(str(i + 1) + ')', a[i])

# Вывести сумму введенных цифр
a = input() 
s = 0
for i in range(len(a)):
    s += int(a[i])
print(s)

#
s = input()
sm = 0
for digit in s:
    sm += int(digit)
print(sm)