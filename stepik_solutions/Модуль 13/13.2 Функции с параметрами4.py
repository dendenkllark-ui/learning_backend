# Перевести Московское время в Пермское

def time(s):
    hours = (int(s[0]) + 2) % 24
    if hours < 10:
        s[0] = '0' + str(hours)
    else:
        s[0] = str(hours)
        s[0] = str(hours)
    print(f'Созвон будет в {':'.join(s)}.')
time(input().split(':'))

#
def time(s):
    hours = (int(s[0]) + 2) % 24
    s[0] = f"{hours:02d}"
    print(f'Созвон будет в {':'.join(s)}.')
time(input().split(':'))

#
def time(s):
    hours = (int(s[0]) + 2) % 24
    s[0] = str(hours).zfill(2)  # Добавил zfill, чтобы 02:00 было с ноликом
    print(f'Созвон будет в {":".join(s)}.')
time(input().split(':'))

#Вывести номер буквы в слове по словорю Unicode
def symbol(s):
    print(*[f'{i}: {ord(i)}' for i in s])
symbol(input())

# #Вывести сколько раз входит символ в строке в алфамитном порядке

def symbol(s):
    s.sort()
    new = []
    for i in s:
        if i not in new:
            print(f'{i}: {s.count(i)}')
            new.append(i)
symbol(list(input().lower()))


#
def symbol(s):
    # Оставляем только уникальные и сразу сортируем их по алфавиту
    unique_s = sorted(set(s))
    
    # Идём циклом по уникальным, а считаем в исходном списке s
    print(*[f'{i}: {s.count(i)}' for i in unique_s], sep='\n')

symbol(list(input().lower()))