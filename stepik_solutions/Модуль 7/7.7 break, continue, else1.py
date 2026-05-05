# #Ищем делители

# num = int(input())
# flag = True
# for i in range(2, num):
#     if num % i == 0:        #  если исходное число делится на какое-либо отличное от 1 и самого себя
#         flag = False
#         break               # останавливаем цикл если встретили делитель числа        

# if flag:  # эквивалентно if flag == True:
#     print('Число простое')
# else:
#     print('Число составное')


# #Проверяем, есть ли цифра 7 в числе

# num = int(input())
# number = num
# flag = False
# while num != 0:
#     last_digit = num % 10
#     if last_digit == 7:
#         flag = True
#         break        # прерываем цикл, так как число гарантированно содержит цифру 7
#     num //= 10

# if flag:  # эквивалентно if flag == True:
#     print('Число', number, 'содержит цифру 7')
# else:
#     print('Число', number, 'не содержит цифру 7')

# #Оператор continue
# for i in range(1, 101):
#     if i == 7 or i == 17 or i == 29 or i == 78:
#         continue  # переходим на следующую итерацию
#     print(i)

# #Наименьший делитель

# num = int(input())
# for i in range (2, num + 1):
#     if num % i == 0:
#         print(i)
#         break

# #Следуй правилам 📋

# num = int(input())
# for i in range (1, num + 1):
#     if (5 <= i <= 9) or (17 <= i <= 37) or (78 <= i <= 87):
#         continue
#     print(i)

#
for x in range(1,int(input())+1):
    if x not in range(5,10) and x not in range(17,38) and x not in range(78,88): print(x)