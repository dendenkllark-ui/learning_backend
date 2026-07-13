
# Является ли треугольник невырожденным

# объявление функции
def is_valid_triangle(a, b, c):
    return (a + b > c) and (a +c > b) and (b +c > a)
# считываем данные
a, b, c = int(input()), int(input()), int(input())
# вызываем функцию
print(is_valid_triangle(a, b, c))

#
def is_valid_triangle(side1, side2, side3):
    sides = [side1, side2, side3]  # создаем список из сторон
    sides.sort()  # сортируем стороны по возрастанию
    return (
        sides[0] + sides[1] > sides[2]
    )  # проверяем, минимальная и средняя стороны больше максимальной
a, b, c = int(input()), int(input()), int(input())
print(is_valid_triangle(a, b, c)) 


# Является ли строка полинтромом

# объявление функции
def is_palindrome(text):
    new = ''
    for i in text:
        if i.isalpha():
            new += i
    return new == new[::-1]

# считываем данные
txt = input().lower()

print(is_palindrome(txt))


# Сравнить слова по длине и по первому символу

def is_one_away(word1, word2):
    if len(word1) != len(word2):
        return False
    count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count += 1
    return count == 1

txt1 = input()
txt2 = input()

# вызываем функцию
print(is_one_away(txt1, txt2))