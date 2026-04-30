#Оператор in

#Цвет настроения синий

s = input()
a = 'синий'
if a in s:
    print('YES')
else:
    print('NO')

#Отдыхаем ли? 

s = input()
a = 'суббота'
b = 'воскресенье'
if a in s or b in s:
    print('YES')
else:
    print('NO')

#Корректный email

s = input()
if '@' in s and '.' in s:
    print('YES')
else:
    print('NO')