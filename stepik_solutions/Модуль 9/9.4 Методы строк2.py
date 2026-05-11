
# #Найти кол-во слов в строке (считаем прообелы)

# s = input()
# print(s.count(' ') + 1)
# #
# s = input()
# print(len(s.split()))

# #Посчитать конкретное кол-во каждыйх букв
# s = input().lower()  # Сразу делаем всю строку строчной
# print(f"Аденин: {s.count('а')}\nГуанин: {s.count('г')}\nЦитозин: {s.count('ц')}\nТимин: {s.count('т')}")

# #сколько раз получено сообщение от Оди
# n = int(input())
# sum = 0
# for i in range(n):
#     mes = input()
#     if mes.count('11') >= 3:
#         sum += 1 
# print(sum)

# ##
# n = int(input())
# cnt = sum(1 for _ in range(n) if input().count("11") >= 3)
# print(cnt)
# ##
# print(sum(input().count('11') >= 3 for _ in range(int(input()))))

#Количество цифр

s = input()
list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
sum = 0
for i in s:
    if i in list:
        sum += 1
print(sum)

#
text = input()
cnt = 0
for i in range(10):
    cnt += text.count(str(i))
print(cnt)

##
data = input()

counter = 0
data2 = '0123456789'
for i in range(len(data)):
    for j in range(len(data2)):
        if data[i] == data2[j]:
            counter += 1
print(counter)

##
s = input()
w = '0123456789'
count = 0
for i in s:
    if i in w:
        count+=1
print(count)

##
s = input()
digits = 0
for i in s:
    if i.isdigit():
        digits += 1
print(digits)