answer = input('Какой язык программирования мы изучаем?')

if answer == 'Python':
    print('Верно! Мы ботаем Python =)')
    print('Python - отличный язык!')
else:
    print('Не совсем так!')
    
    num1, num2, num3 = int(input()), int(input()), int(input())

counter = 0  
if num1 % 2 == 0:
    counter = counter + 1  
if num2 % 2 == 0:
    counter = counter + 1  
if num3 % 2 == 0:
    counter = counter + 1  

print(counter)