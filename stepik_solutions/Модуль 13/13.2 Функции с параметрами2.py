# Вывести ФИО через функцию

def name(n, f, o):
    print(f[0]+n[0]+o[0])
n = input().capitalize()
f = input().capitalize()
o = input().capitalize()
name(n, f, o)

#
def name(n, f, o):
    print((f[0] + n[0] + o[0]).upper())
n = input()
f = input()
o = input()
name(n, f, o)

# Посчитать кол-во букв в верхнем регистре в строке

def counts(s):
    up = 0
    down = 0
    for i in s:
        if i.isupper():
            up += 1
        elif i.islower():
            down += 1
    print(f'Букв в верхнем регистре: {up}\nБукв в нижнем регистре: {down}')

counts(input())


# Принять одно число и посчитать сумму его цифр

def sum(s):
    a = 0
    for i in s:
        a += int(i)
    print(a)
sum(input())

#
def get_sum(s):
    # Превращаем каждый символ в int прямо внутри встроенного sum()
    print(sum(int(i) for i in s))
get_sum(input())
        
    
