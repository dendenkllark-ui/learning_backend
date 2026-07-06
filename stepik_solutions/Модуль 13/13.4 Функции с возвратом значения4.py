
# Ввести число с плавающей точной но вывести целое в сторону математического огругления

def math_round_to_int(num):
    if num - int(num) == 0.5:
        return int(num) + 1
    return round(num)
num = float(input())
print(math_round_to_int(num))

#
from math import ceil, floor
def math_round_to_int(num):
    if num - int(num) >= 0.5:
        return ceil(num)
    else:
        return floor(num)
num = float(input())
print(math_round_to_int(num))


# Вывести список всех делителей числа

def get_factors(num):
    m = []
    for i in range(1, num + 1):
        if num % i == 0:
            m.append(i)
    return m    
n = int(input())
print(get_factors(n))

def get_factors(num):
    return [i for i in range(1, num + 1) if num % i == 0]
n = int(input())
print(get_factors(n))

#
def get_factors(num):
    return [i for i in range(1, num // 2 + 1) if num % i == 0] + [num]
n = int(input())
print(get_factors(n))

# Вывести кол-во делителей числа

def get_factors(num):
    return len([i for i in range(1, num // 2 + 1) if num % i == 0] + [num])
n = int(input())
print(get_factors(n))