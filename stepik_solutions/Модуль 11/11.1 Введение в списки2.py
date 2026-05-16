# Подается число, вывести в список эту последовательность

n = int(input())
print((list(range(1, n + 1))))

# Вывести список букв n-раз начиная с a

n = int(input())
print(list(chr(i) for i in range(ord("a"), ord("a") + n)))

#
n = int(input())
s = ""
for i in range(n):
    s += chr(ord("a") + i)
print(list(s))


# Списко нечетных чисел от 1 до n

n = int(input())
print(list(range(1, n + 1, 2)))

#
n = int(input())
ls = [i for i in range(n + 1) if i % 2 != 0]
print(ls)

# Создать список из введенной строки, добавляя туда каждый второй элемент

n = input()
print(list(n[i] for i in range(0, len(n), 2)))

#
things = input()
things_to_take = list(things[::2])
print(things_to_take)

#
print(list(input()[::2]))
