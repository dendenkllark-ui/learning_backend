#
zeros = []
for i in range(10):
    zeros.append(0)
#
zeros = [0] * 10

#
numbers = []
for i in range(10):
    numbers.append(i)

#
numbers = [i for i in range(10)]

#
zeros = [0 for i in range(10)]

#
cubes = [i ** 3 for i in range(10, 21)]

#
chars = [c for c in 'abcdefg']
print(chars)


#В списочном выражении можно использовать вложенные циклы:

numbers = [i * j for i in range(1, 5) for j in range(2)]
print(numbers)  # [0, 1, 0, 2, 0, 3, 0, 4]