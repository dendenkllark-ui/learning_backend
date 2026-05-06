# Часы
for hours in range(24):
    for minutes in range(60):
        for seconds in range(60):
            print(hours, ":", minutes, ":", seconds)

# Прерывание вложенного цикла

for i in range(3):
    for j in range(3):
        if i == j:
            break
        print(i, j)
#
for i in range(3):
    for j in range(3):
        if i == j:
            continue
        print(i, j)

# Таблица из звездочек

for i in range(8):
    for j in range(6):
        print('*', end='')
    print()

# Треугольник
for i in range(8):
    for j in range(i + 1):
        print('*', end='')
    print()

