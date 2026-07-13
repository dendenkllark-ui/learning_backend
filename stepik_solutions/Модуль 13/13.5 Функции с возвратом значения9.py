

# # Проверить является ли пароль надежным

# Решение через логическое отрицание
# объявление функции
def is_password_good(text):
    is_valid = (
        text.isalnum()
        and not text.isalpha()
        and not text.isdigit()
        and not text.isupper()
        and not text.islower()
)
    if len(text) >= 8 and is_valid:
        return True
    else:
        return False
# считываем данные
txt = input()
# вызываем функцию
print(is_password_good(txt))

# Решение в лоб
def is_password_good(text):
    if len(text) < 8:
        return False
    has_upper = False
    has_lower = False
    has_digit = False
    # Ищем нужные символы в лоб
    for char in text:
        if char.isupper():
            has_upper = True
        if char.islower():
            has_lower = True
        if char.isdigit():
            has_digit = True
    # Пароль хороший, если нашли все три типа символов
    return has_upper and has_lower and has_digit
txt = input()
print(is_password_good(txt))