

# определить состоит ли сообщение из пробелов или пустых строк
n = int(input())
for i in range(1, n + 1):
    text = input()
    if text.isspace() or text == '':
        text = 'COMMENT SHOULD BE DELETED'
    print(f'{i}: {text}')

# Тоже самое только через if not .strip() = удаляет все пробелы, если строка пуска, not вернет True

n = int(input())
for i in range(1, n + 1):
    text = input()
    if not text.strip():
        text = 'COMMENT SHOULD BE DELETED'
    print(f'{i}: {text}')



# Прооверить никнейм на условия

n = input()
if n.startswith('@') and 5 <= len(n) <= 15 and n[1:].isalnum() and n[1:] == n[1:].lower():
    print('Correct')
else:
    print('Incorrect')

#
s = input()

if (
    s.startswith('@')
    and 5 <= len(s) <= 15
    and s[1:].isalnum()
    and s == s.lower()
):
    print('Correct')
else:
    print('Incorrect')


# Составить автомобильный номер
    
n = input()
x = 'АВЕКМНОРСТУХ'
if 9 <= len(n) <= 10 and n[6] == '_':
    if n[0] in x and n[4] in x and n[5] in x:
        if n[1:4].isdigit() and n[7:].isdigit():
            print('YES')
        else:
            print('NO')
    else:
            print('NO')
else:
            print('NO')

#
s = input()
flag = 'NO'
correct_letters = 'АВЕКМНОРСТУХ'

if 9 <= len(s) <= 10:
    letters = s[0] + s[4:6]
    digits = s[1:4] + s[7:]
    underscore = s[6]

    if digits.isdigit() and underscore == '_':
        flag = 'YES'

    for c in letters:
        if c not in correct_letters:
            flag = 'NO'
            break


n = input()
x = 'АВЕКМНОРСТУХ'
if 9 <= len(n) <= 10 and n[6] == '_':
    for i in n[0] + n[4:6]:
        if i not in x:
            print('NO')
            break
    else:
        if n[1:4].isdigit() and n[7:].isdigit():
            print('YES')
        else:
            print('NO')
else:
    print('NO')

####
n = input()
x = 'АВЕКМНОРСТУХ'
if 9 <= len(n) <= 10 and n[6] == '_':
    for i in n[0] + n[4:6]:
        if i not in x:
            print('NO')
            break
    else:
        for i in n[1:4] + n[7:]:
            if not i.isdigit():
                print('NO')
                break
        else:
            print('YES')
else:
    print('NO')

###
n = input()
x = 'АВЕКМНОРСТУХ'
valid = True

if not (9 <= len(n) <= 10 and n[6] == '_'):
    valid = False
else:
    for i in n[0] + n[4:6]:
        if i not in x:
            valid = False
    
    # Проверка цифр
    if not (n[1:4].isdigit() and n[7:].isdigit()):
        valid = False

print('YES' if valid else 'NO')


