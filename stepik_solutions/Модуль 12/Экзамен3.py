# Является ли строка верным телефонным номером

a = input().split('-')
all_digits = True
for i in a:
    if not i.isdigit():
        all_digits = False
if not all_digits:
    print("NO")
elif len(a) == 4:
    if a[0] == '7' and len(a[1]) == 3 and len(a[2]) == 3 and len(a[3]) == 4:
        print("YES")
    else:
        print("NO")
elif len(a) == 3:
    if len(a[0]) == 3 and len(a[1]) == 3 and len(a[2]) == 4:
        print("YES")
    else:
        print("NO")
else:
    print("NO")


# Лушчий вариант
a = input().split("-")
lens = [len(i) for i in a]
if lens == [1, 3, 3, 4] and "".join(a).isdigit() and a[0] == "7":
    print("YES")
elif lens == [3, 3, 4] and "".join(a).isdigit():
    print("YES")
else:
    print("NO")


#
# Читаем строку целиком (без .strip(), так как пробелы — это некорректные символы)
a = input().split('-')
# Собираем длины всех блоков
lengths = [len(i) for i in a]
# Проверяем, что абсолютно все символы во всех блоках — это цифры
all_digits = all(i.isdigit() for i in a)
# Финальная проверка строго по условию задачи
if all_digits and ((lengths == [1, 3, 3, 4] and a[0] == '7') or lengths == [3, 3, 4]):
    print("YES")
else:
    print("NO")



# *Решение, если подается только подходящая по кол-ву слов в строке*

a = input().split('-')
# Собираем длины только тех блоков, которые состоят из цифр
lengths = [len(i) for i in a if i.isdigit()]
# Проверяем шаблоны: либо [1, 3, 4, 4] при условии, что первая — '7', либо [3, 4, 4]
if (lengths == [1, 3, 3, 4] and a[0] == '7') or lengths == [3, 3, 4]:
    print("YES")
else:
    print("NO")










    
