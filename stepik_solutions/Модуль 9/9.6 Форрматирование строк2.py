##
a = 2010
b = '10k'
c = 'Bitcoin'
s = 'In {0}, someone paid {1} {2} for two pizzas.'.format(a, b, c)
print(s)

##
a = 2010
b = '10K'
c = 'Bitcoin'
print(f'In {a}, someone paid {b} {c} for two pizzas.')

#
s = f'In {2010}, someone paid {'10K'} {'Bitcoin'} for two pizzas.'
print(s)

# Курсы валют

a = input()
b = float(input())
c = float(input())
print(f'На {a}: 1€ = {b}₽, 1¥ = {c}₽')

## Сумма кубов/Куб суммы
a = int(input())
b = int(input())
print(f'''Для чисел {a} и {b}:
  Сумма кубов: {a}**3 + {b}**3 = {a**3 + b**3}
  Куб суммы: ({a} + {b})**3 = {(a + b)**3}''')


##
day = int(input())
w = float(input())
x = 100 - (0.2 * day)
if w > x:
    print(f'''Что-то пошло не так
#{day} ДЕНЬ: ТЕКУЩИЙ ВЕС = {w} кг, ЦЕЛЬ по ВЕСУ = {x} кг''')
else:
    print(f'''Все идет по плану
#{day} ДЕНЬ: ТЕКУЩИЙ ВЕС = {w} кг, ЦЕЛЬ по ВЕСУ = {x} кг''')
