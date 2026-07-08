
# #Вывести индекс слова в списке, если его нет, вывести ошибку

def get_last_index(data, value):
    if value in data:
        new = data[::-1]
        return len(data) - 1 - new.index(value)
    else:
        return 'ERROR!'
data = eval(input())
value = eval(input())
print(get_last_index(data, value))

#
def get_last_index(data, value):
    res = 'ERROR!'
    for i in range(len(data)):
        if data[i] == value:
            res = i
    return res
data = eval(input())
value = eval(input())
print(get_last_index(data, value))


# Вернуть список всех вхождений символа и исходном списке

# объявление функции
def find_all(target, symbol):
    a = []
    for i in range(len(target)):
        if target[i] == symbol:
            a.append(i)
    return a
    # return [i for i in range(len(target)) if target[i] == symbol]
s = input()
char = input()

print(find_all(s, char))



# Принять два списка и вывести один отсортированный

# объявление функции
def merge(list1, list2):
    a = list1 + list2
    a.sort()
    return a

# считываем данные
numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]

# вызываем функцию
print(merge(numbers1, numbers2))

# Через сортировку выбором

def merge(list1, list2):
    list1.extend(list2)
    n = len(list1)
    for i in range(n):
        max_dig = max(list1[: n - i])
        max_dig_ind = list1.index(max_dig)
        extracting_dig = list1.pop(max_dig_ind)
        list1.append(extracting_dig)
    list1.reverse()
    return list1
list1 = [int(dig1) for dig1 in input().split()]
list2 = [int(dig2) for dig2 in input().split()]
print(merge(list1, list2))
