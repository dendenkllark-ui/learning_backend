# Вывести 17 элемент списка
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
print(primes[16])

#
s = [12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324]

print(sum([max(s), min(s)]))

# Среднее арифметическое всех элементов списка

x = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
average = sum(x) / len(x)
print(average)


# Заменить слова в списке

x = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
x[x.index('Green')] = 'Зеленый'
x[x.index('Violet')] = 'Фиолетовый'

print(x)

# Вывести список в обратном порядке

x = ['Chinese', 'Spanish', 'English', 'Hindi', 'Arabic', 'Bengali', 'Portuguese', 'Russian', 'Japanese', 'Lahnda']
print(x[::-1])

# Конкатенация списков


x = [1, 2, 3]
y = [6]
z = [7, 8, 9, 10, 11, 12, 13]

print(x*2 + y*9 + z)