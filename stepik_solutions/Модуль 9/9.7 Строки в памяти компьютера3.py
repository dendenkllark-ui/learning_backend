

#Расчитать стоимость строки

a = input()
x = 0
for i in a:
    i = ord(i)
    x += i
print(f"Текст сообщения: '{a}'\nСтоимость сообщения: {x*3}🐝")

#
s = input()
total = sum(ord(i) for i in s) * 3
print(f"Текст сообщения: '{s}'")
print(f'Стоимость сообщения: {total}🐝')

# Стоимость строки, если буквы русские, а не английские

text = input()
eng = "eyopaxcETOPAHXCBM"
rus = "еуорахсЕТОРАНХСВМ"
old = 0
new = 0
for i in text:
    cost = ord(i)
    old += cost * 3
    if i in eng:
        x = eng.index(i)
        new_cost = ord(rus[x])
        new += new_cost * 3
    else:
        new += cost * 3
print(f"Старая стоимость: {old}🐝")
print(f"Новая стоимость: {new}🐝")

