
# Правильная скобочная последовательность 

# объявление функции
def is_correct_bracket(text):
    count = 0
    for i in text:
        if i == '(':
            count += 1
        elif i == ')':
            count -= 1
        if count < 0:
            return False
    if count == 0:
        return True
    else:
        return False
txt = input()
print(is_correct_bracket(txt))

#
def is_correct_bracket(text):
    cnt = 0
    for el in text:
        if el == "(":
            cnt += 1
        else:
            cnt -= 1
            
        if cnt == -1:
            break
            
    return cnt == 0
txt = input()
print(is_correct_bracket(txt))

# Через while

def is_correct_bracket(text):
    while "()" in text:
        text = text.replace("()", "")
    return text == ""
txt = input()
print(is_correct_bracket(txt))


# Проверка пароля на условия

# объявление функции
def is_valid_password(pas):
   
    if len(pas) != 3:
        return False
    
    part1= pas[0]
    part2 = int(pas[1])
    part3 = int(pas[2])
#1
    flag1 = part1 == part1[::-1]
#2
    flag2 = True
    if part2 <= 1:
        flag2 = False
    else:
        for i in range(2, int(part2**0.5) + 1):
            if part2 % i == 0:
                flag2 = False
                break
#3
    flag3 = part3 % 2 == 0

    return flag1 and flag2 and flag3

psw = input().split(':')

print(is_valid_password(psw))