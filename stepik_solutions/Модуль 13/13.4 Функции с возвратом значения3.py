# # Работа со списком внутри функции

# def do_something(numbers):
#     result = 1
#     for i in numbers:
#         result *= i
#     return result
# print(do_something([2, 2, 2, 2]))


# Перевести мили в киллометры

# def convert_to_miles(km):
#     return km * 0.6214
# num = int(input())
# print(convert_to_miles(num))

# # Обвернуть строку в теги

# # объявление функции
# def code_format(text):
#     return f'<code>{text}</code>'
# text = input()
# print(code_format(text))


# Вывести кол-во дней в месяце


def get_days(a):
    if a in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif a in (4, 6, 9 , 11):
        return 30
    if a == 2:
        return 28
num = int(input())
print(get_days(num))