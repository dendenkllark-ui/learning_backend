
# Быстрое слияние двух отсортированных списков в один

def quick_merge(list1, list2):
    result = []
    p1 = 0  # указатель на первый элемент списка list1
    p2 = 0  # указатель на первый элемент списка list2
    while p1 < len(list1) and p2 < len(list2):  # пока не закончился какой-нибудь из списков
        if list1[p1] <= list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1
    if p1 < len(list1):   # прицепление остатка
        result += list1[p1:]
    else:                 # иначе прицепляем остаток другого списка
        result += list2[p2:]
    return result
list1 = [3, 10, 11, 12, 47, 57, 58, 63, 77, 79, 80, 95]
list2 = [0, 11, 12, 20, 24, 26, 47, 48, 53, 65, 70, 81, 84, 84, 90]
list3 = quick_merge(list1, list2)
print(list3)

# Ввести число - кол-во списков, которые нужно объединить и отсортировать



def a(n, res):
    while n != 0:
        m = list(input().split())
        m_digit = [int(i) for i in m]
        res.extend(m_digit)
        n -= 1
    res.sort()
    return res

n = int(input())
res = []
print(*a(n, res))

# 
def quick_merge(n):
    lst = []
    for i in range(n):
        lst += input().split()
    print(*sorted(int(i) for i in lst))
quick_merge(int(input()))


# Через алгоритм соритровки

# берём из теории уже реализованную функцию быстрой сортировки
def quick_merge(list1, list2):
    result = []

    p1 = 0  # указатель на первый элемент списка list1
    p2 = 0  # указатель на первый элемент списка list2

    while p1 < len(list1) and p2 < len(list2):  # пока ни один из списков не закончился
        if list1[p1] <= list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1

    if p1 < len(list1):   # прицепление остатка
        result += list1[p1:]
    else:                 # иначе прицепляем остаток другого списка
        result += list2[p2:]
    
    return result

# принимаем кол-во строк
n = int(input())

# формируем из первой строки список чисел и возьмём
# этот первый список за основу для результирующего списка
res = [int(num) for num in input().split()]

# принимаем n - 1 строк (потому что первую строку мы уже приняли)
for _ in range(n - 1):
    # принимаем текущую строку и формируем из неё список чисел
    cur_list = [int(num) for num in input().split()]
    
    # объединяем результирующий список и текущий список
    # и записываем этот новый отсортированный список в качестве
    # результирующего списка
    res = quick_merge(res, cur_list)

# выводим результирующий список
print(*res)