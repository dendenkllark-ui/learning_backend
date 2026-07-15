
# Продолжение задачи на проверку пароля

def is_palindrome(num):
    return str(num) == str(num)[::-1]

def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
        
    return True

def is_even(num):
    return num % 2 == 0

def is_valid_password(password):
    seq = password.split(":")
    if len(seq) == 3:
        seq = [int(el) for el in seq]
        a, b, c = seq[0], seq[1], seq[2]
        return is_palindrome(a) and is_prime(b) and is_even(c)
    return False

psw = input()

print(is_valid_password(psw))


#

def is_prime(num):
    cnt = 1
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            cnt += 1
    return cnt <= 2 and num != 1

def is_valid_password(password):
    password = password.split(':')
    if len(password) != 3:
        return False
    if password[0][:] != password[0][::-1]:
        return False
    if is_prime(int(password[1])) is False:
        return False
    if int(password[2]) % 2 != 0:
        return False
    else:
        return True

psw = input()

print(is_valid_password(psw))
