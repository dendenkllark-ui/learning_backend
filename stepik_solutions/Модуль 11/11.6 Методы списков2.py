

# Посчитать кол-во артиклей в тексте

s = input().lower().split()
sum = 0
for n in s:
    if n == 'a' or n == 'an' or n == 'the':
        sum += 1
print(f'Общее количество артиклей: {sum}')

s = input().lower().split()
c1 = s.count("a")
c2 = s.count("an")
c3 = s.count("the")
sum = c1 + c2 + c3
print(f'Общее количество артиклей: {sum}')

#
lst = list(input().lower().split())
lst_art = ["a", "an", "the"]
total = 0
for i in lst_art:
    for j in lst:
        if i == j:
            total += 1
print(f"Общее количество артиклей: {total}")

# через удаление символов пунктуации
s = input().lower().split()
clean_words = []
for word in s:
    # Отрезаем от каждого слова знаки препинания, если они прилипли сбоку
    clean_word = word.strip('.,!?";:')
    clean_words.append(clean_word)
# Теперь считаем артикли в чистом списке clean_words
c1 = clean_words.count("a")
c2 = clean_words.count("an")
c3 = clean_words.count("the")
print(f'Общее количество артиклей: {c1 + c2 + c3}')

# через замену символов пунктуации на пробелы
s = input().lower()
# Очищаем строку от популярных знаков препинания
s = s.replace('.', '').replace(',', '').replace('!', '').replace('?', '')
words = s.split() # Теперь бьем на слова чистый текст
c1 = words.count("a")
c2 = words.count("an")
c3 = words.count("the")
total_sum = c1 + c2 + c3
print(f'Общее количество артиклей: {total_sum}')


# через модуль re
import re
# re.sub заменяет все знаки препинания на пустоту
s = input().lower()
s = re.sub(r'[^\w\s]', '', s) 
words = s.split()
c1 = words.count("a")
c2 = words.count("an")
c3 = words.count("the")
print(f'Общее количество артиклей: {c1 + c2 + c3}')




