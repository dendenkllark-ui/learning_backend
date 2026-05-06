# Решение уравнениия  12x+13y=777

total = 0
for x in range(1, 65):
    for y in range(1, 60):
        if 12 * x + 13 * y == 777:
            total += 1
            print('x =', x, 'y =', y)
print('Общее количество натуральных решений =', total)

# Решение уравнениия  x2+y2+z2=2020.

total = 0
for x in range(1, 45):
    for y in range(1, 45):
        for z in range(1, 45):
            if x ** 2 + y ** 2 + z ** 2 == 2020:
                total += 1
                print('x =', x, 'y =', y, 'z =', z)
print('Общее количество натуральных решений =', total)

# Решение уравнениия 28n+30k+31m=365.

total = 0
for n in range(1, 14):
    for k in range(1, 13):
        for m in range(1, 12):
            if n * 28 + k * 30 + m * 31 == 365:
                total += 1
                print('n =', n, 'k =', k, 'm =', m)
print('Общее количество натуральных решений =', total)

#Решение уравнениия x * 10 + y * 5 + z * 0,5

total = 0
for x in range(1, 11):
    for y in range(1, 21):
        for z in range(1, 201):
            if x * 10 + y * 5 + z * 0.5 == 100:
                if x + y + z == 100:
                    total += 1
                    print('x =', x, 'y =', y, 'z =', z)
print('Общее количество натуральных решений =', total)

# Гипотеза Эйлера о сумме степеней 🌶️
#
for a in range(1, 151):
    for b in range(a, 151):
        for c in range(b, 151):
            for d in range(c, 151):
                sum = a**5 + b**5 + c**5 + d**5
                for e in range(d + 1, 151):
                    if sum == e**5:
                        print(a + b + c + d + e)

#
for a in range(1, 151):
    for b in range(a, 151):
        for c in range(b, 151):
            for d in range(c, 151):
                sum = a**5 + b**5 + c**5 + d**5
                e = int(sum**(1/5))
                if sum == e**5:
                    print(a, b, c, d, e)
                    print(a + b + c + d + e)
                    break

###
# 1. Готовим "шпаргалку" (кэш)
# Создаем список, где индекс — это число, а значение — его 5-я степень
powers = [i**5 for i in range(151)]
# Для супер-быстрой проверки преобразуем список в множество (set)
# Поиск в множестве в Python происходит мгновенно (O(1))
powers_set = set(powers)
# 2. Запускаем 4 вложенных цикла
for a in range(1, 151):
    for b in range(a, 151):
        for c in range(b, 151):
            for d in range(c, 151):
                # Складываем уже готовые значения из списка
                total_sum = powers[a] + powers[b] + powers[c] + powers[d]
                
                # 3. Мгновенно проверяем, есть ли такая сумма в нашем наборе
                if total_sum in powers_set:
                    # Если нашли, ищем само число e через индекс в списке
                    e = powers.index(total_sum)    # e = int(sum**(1/5))
                    print(f"Найдено: a={a}, b={b}, c={c}, d={d}, e={e}")
                    print("Ответ (сумма):", a + b + c + d + e)
                    # Выходим из программы, так как ответ один
                    exit()
