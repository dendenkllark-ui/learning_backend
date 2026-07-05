# # Нарисовать прямоугольник из символов "*" с заданной шириной и высотой через функцию.

# def draw_box():
#     for _ in range(5):
#         print('*' * 7)
# draw_box()
# print()
# draw_box()
# print()
# draw_box()

#
# # объявление функции
# def print_message():
#     print('Я - Артур,')
#     print('король британцев. ')
# # вызов функции
# print_message()


# # Функция ничего неделания (заглушка)
# def do_nothing():
#     pass

# # Нарисовать звездный прямоуголник

# def draw_box():
#     for i in range(1, 15):
#         if i == 1 or i == 14:
#             print('*' * 10)
#         else:
#             print(f"*{' ' * 8}*")
# draw_box()

# #
# def draw_box():
#     print('*' * 10)
#     for _ in range(12):
#         print(f"*{' ' * 8}*")
#     print('*' * 10)
# draw_box()

# #
# def draw_box():
#     middle_rows = f"*{' ' * 8}*\n" * 12
#     print(f"{'*' * 10}\n{middle_rows}{'*' * 10}")
# draw_box()

# Вывести звездный треугольник

def draw_triangle():
    for i in range(1, 11):
        print(i*'*')
draw_triangle()

#
def triangle():
    print(*["*" * i for i in range(1, 11)], sep="\n")
triangle()

# Через join
def draw_triangle():
    print('\n'.join(i * '*' for i in range(1, 11)))

draw_triangle()