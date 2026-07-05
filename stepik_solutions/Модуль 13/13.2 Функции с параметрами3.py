#Принять строку с дефисами, отсортировать её в порядке возрастания 
#по строке и вывести с дефисами

def my_sort(s):
    s.sort()
    print(*s, sep='-')
my_sort(input().split('-'))

#
def print_sorted_hyphen(s):
    print('-'.join(sorted(s)))
print_sorted_hyphen(input().split('-'))

#
def print_sorted_hyphen(s):
    print(*(sorted(s.split('-'))), sep='-')
print_sorted_hyphen(input())


# Звездный треуголник по возрастанию и убыванию

def angle(f, b):
    mid = (b//2)+1
    for i in range(1, mid + 1):
        print(f * i)
    for i in range(mid - 1, 0, -1):
        print(f * i)
angle(input(), int(input()))

#
def angle(f, b):
    mid = (b // 2) + 1
    # 1. Создаем список строк для первой половины
    up = [f * i for i in range(1, mid + 1)]
    # 2. Создаем список строк для второй половины
    down = [f * i for i in range(mid - 1, 0, -1)]
    # Складываем два списка в один и склеиваем через перенос строки
    print('\n'.join(up + down))
angle(input(), int(input()))

#
def angle(f, b):
    mid = b // 2
    # Генерируем сразу всю фигуру за один проход
    triangle = [f * ((mid + 1) - abs(i)) for i in range(-mid, mid + 1)]
    print('\n'.join(triangle))
angle(input(), int(input()))