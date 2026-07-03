#
# key = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 
#    'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
# new_keywords = [x for x in key if len(x) >= 5]
# print(new_keywords)

#Вывести список палиндромов в диапазоне

# palindromes = [i for i in range (100, 1001) if str(i) == str(i)[::-1]]
# print(palindromes)

# Вывести слова в столбик из введенной строки 

# x = input().split()
# print(*x, sep='\n')

# #
# print(*input().split(), sep='\n')

# #
# n = int(input())
# x = [i**2 for i in range(1, n + 1)]
# print(*x, sep='\n')

# #
# print(*[i ** 2 for i in range(1, int(input()) + 1)], sep="\n")


#Вывести куды чисел, введенных в одну строку через пробел

# a = input().split()
# x = [int(i)**3 for i in a if i.lstrip('-').isdigit()]
# print(*x)

# #
# print(*[int(i) ** 3 for i in input().split()])


# Вывести все цифромые символы в строке, введенной пользователем

# a = input()
# x = [i for i in a if i.isdigit()]
# print(*x, sep='') 

# #
# print(*[i for i in input() if i.isdigit()], sep="")


# вывести квадраты чисел, кроме определенных

a = input().split()
x = [int(i)**2 for i in a if int(i) % 2 == 0 and (int(i)**2) % 10 != 4]
print(*x)

#
num = [int(i) for i in input().split()]
x = [a**2 for a in num if a % 2 == 0 and (a**2) % 10 != 4]
print(*x)

# как одну строку удобно разбить
print(
    *[
        int(i) ** 2
        for i in input().split()
        if int(i) % 2 == 0 and int(i) ** 2 % 10 != 4
    ]
)
