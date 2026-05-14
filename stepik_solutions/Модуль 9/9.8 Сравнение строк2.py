


# Является ли введенное кол-во классов в школе верным номером
n = int(input())

for i in range(n):
    a = input()
    if len(a) == 2 and '0' <= a[0] <= '9' and 'А' <= a[1] <= 'П':
        print('YES')
    else:
        print('NO')     


# Сортировка книг в определенном порядке

n = int(input())
for i in range(n):
    a = input()

n = int(input())

original_books = []
formatted_books = []

for _ in range(n):
    line = input()
    # Запоминаем исходный порядок строк для финального сравнения
    original_books.append(line)
    # Извлекаем фамилию и название
    author = line.split()[0]
    title = line.split('«')[1].split('»')[0]
    # Сохраняем в список в виде пары: [Автор, Название, Исходная_строка]
    formatted_books.append([author, title, line])
# Python САМ умеет сортировать вложенные списки:
# Сначала он сортирует по первому элементу (автору),
# а если они одинаковые — автоматически по второму (названию).
# Инициалы при этом вообще не участвуют в сортировке!
formatted_books.sort()
# Собираем обратно список строк, но уже гарантированно отсортированный
sorted_books = [book[2] for book in formatted_books]
# Если исходный порядок совпадает с идеальным по мнению Python — выводим YES
if original_books == sorted_books:
    print("YES")
else:
    print("NO")

##
n = int(input())
# переменные для хранения предыдущей фамилии автора и названия книги
previous_book = ''
# переменная флага указывает, сохранен ли порядок сортировки книг:
is_ordered = 'YES'

for i in range(n):
    s = input()
    # извлекаем фамилию автора до первого пробела
    current_surname = s[: s.find(' ')]
    # извлекаем название книги между кавычками «»
    current_title = s[s.find('«') + 1 : s.rfind('»')]
    # склеиваем фамилию автора и название книги
    current_book = current_surname + current_title
    # если текущая книга меньше предыдущей
    # то порядок сортировки нарушен
    if current_book < previous_book:
        is_ordered = 'NO'
    # обновляем предыдущие значения книги на текущие
    previous_book = current_book

print(is_ordered)