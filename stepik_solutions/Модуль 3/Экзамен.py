#Задача на квадрат из звездочек
# print("""*****************
# *               *
# *               *
# *****************""")

# a = 17
# print("*" * a)
# print("*" + " " * (a - 2) + "*")
# print("*" + " " * (a - 2) + "*")
# print("*" * a)

# a = 17
# empty_line = f"*{' ' * (a - 2)}*"
# border = "*" * a

# print(border, empty_line, empty_line, border, sep="\n")

#Квадрат суммы и сумма квадратов

# a = int(input())
# b = int(input())
# print(f'Квадрат суммы {a} и {b} равен {(a+b)**2}\nСумма квадратов {a} и {b} равна {a**2 + b**2}')

#Задача на большое число

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# print(a**b + c**d)

#Размножение n-ок
n = int(input())
n1 = 11 * n
n2 = 111 * n
n3 = n + n1 + n2
print(n3)

number = int(input())
a = number
aa = int(str(number) * 2)
aaa = int(str(number) * 3)
print(a + aa + aaa)

a1 = input() # 1
a11 = a1 + a1
a111 = a1 + a1 + a1
print(int(a111) + int(a1) + int(a11))

print()