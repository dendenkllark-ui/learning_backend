

# # Удалить нечетные индексы

# n = int(input())
# s = []
# for i in range(n):  
#     num = int(input())
#     if i % 2 == 0:  
#         s.append(num) 
# print(s)

# # Создаем список, а потом удаляем нечетные индексы

# n = int(input())
# s = []
# for _ in range(n):
#     s.append(int(input()))
# for i in range(len(s) - 1, -1, -1):
#     if i % 2 != 0:  
#         del s[i]    
# print(s)


# # Подать n строк, затем вывести их в виде списка, каждую отдельную букву

# n = int(input())
# s = []
# for _ in range(n):
#     s.extend(input())
# print(s)

# Подается n строк, и затем выводится k-ая буква каждого слова

n = int(input())
s = []
a = ''
for _ in range(n):
    x = input()
    s.append(x) 
k = int(input()) - 1
for i in range(n):
    if len(s[i]) > k:
        a += s[i][k]
print(a)
