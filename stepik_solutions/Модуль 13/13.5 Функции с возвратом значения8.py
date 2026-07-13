
# # Перевести строку из верблюжьего языка в змениный

# def convert_to_python_case(text):
#     result = []
#     for i in range(len(text)):
#         char = text[i]
#         # Если буква заглавная и она НЕ первая в строке
#         if char.isupper() and i > 0:
#             result.append("_")  # Добавляем дорожку-подчеркивание
#         result.append(char.lower())  # Добавляем саму букву, сделав её маленькой
#     # Склеиваем список символов обратно в одну строку
#     return "".join(result)
# # считываем данные
# text = input()
# # вызываем функцию
# print(convert_to_python_case(text))


# # Число простое или сотавное?

# # объявление функции
# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int((num**0.5) + 1)):
#         if num % i == 0:
#             return False
#     return True
# # считываем данные
# n = int(input())

# # вызываем функцию
# print(is_prime(n))


# Выернуть следующее простое число просто введенного числа

# объявление функции
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def next_prime(num):
    next = num + 1
    while True:
        if is_prime(next):
            return next 
        next += 1

# считываем данные
n = int(input())

# вызываем функцию
print(next_prime(n))


#
def get_next_prime(num):
    o = num + 1
    x = 0
    while x == 0:
        for i in range(2, o + 1):
            if o % i == 0 and o != i:
                o += 1
                break
            elif o % i == 0 and o == i:
                x += 1
                break
            else:
                continue
    return o