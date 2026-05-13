#==================================================================================================================

# Метод format()  не нужно отдельно переводить числа в строку

birth_year = 1992
text = 'My name is Timur, I was born in {}'.format(birth_year)
print(text)

#
birth_year = 1992
name = 'Timur'
profession = 'math teacher'
text = 'My name is {}, I was born in {}, I work as a {}.'.format(name, birth_year, profession)
print(text)
# выводит:
# My name is Timur, I was born in 1992, I work as a math teacher.

# Параметр name встает в заполнителе {0}, параметр birth_year – в заполнителе {1} и т.д. 
# Мы можем использовать одно и то же число в нескольких заполнителях или не использовать совсем, 
# а также мы можем использовать числа в разном порядке.
name = 'Timur'
city = 'Moscow'
text1 = 'My name is {0}-{0}-{0}!'.format(name, city)
text2 = '{1} is my city and {0} is my name!'.format(name, city)
print(text1)
print(text2)
# выводит:
# My name is Timur-Timur-Timur!
# Moscow is my city and Timur is my name!

#==================================================================================================================

# f-строки

first_name = 'Taylor'
second_name = 'Swift'
country = 'USA'
birth_date = '1989/12/13'
birth_place = 'West Reading, Pennsylvania'
text = '{0} {1} is a very famous singer from the {2}. She was born on {3} in {4}.'.format(first_name, second_name, country, birth_date, birth_place)
print(text)
# выводит:
# Taylor Swift is a very famous singer from the USA. She was born on 1989/12/13 in West Reading, Pennsylvania.

first_name = 'Taylor'
last_name = 'Swift'
country = 'USA'
birth_date = '1989/12/13'
birth_place = 'West Reading, Pennsylvania'
text = f'{first_name} {last_name} is a very famous singer from the {country}. She was born on {birth_date} in {birth_place}.'
print(text)

print(f'5 + 2 = {5 + 2}')
print(f'5 - 2 = {5 - 2}')
print(f'5 * 2 = {5 * 2}')
print(f'5 / 2 = {5 / 2}')
