# #
# numbers = [1, 2, 3, 4, 5]
# numbers[2] = 99
# print(numbers)

# #
# numbers = list(range(3))
# print(numbers)

# #
# numbers = [10] * 5
# print(numbers)

# #
# numbers = list(range(1, 10, 2))
# for i in numbers:
#     print(i, end='*')

# #
# numbers = [1, 2, 3, 4, 5]
# print(numbers[-2])

numbers = [1, 2, 3, 4, 5]
my_list = numbers[:-1]
print(my_list)


# #Вывести список четных чисел

# n = int(input())
# x = []
# for i in range(2, n+1, 2):
#     x.append(i)
# print(x)

# # В одну строчку
# print(list(range(2, int(input()) + 1, 2)))
# #
# print([i for i in range(2, int(input()) + 1, 2)])
