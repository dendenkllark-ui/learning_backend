##
# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(s[0:12])
##
# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(s[-9::])
# #
# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(s[0::7])
# #
# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(s[::-1])

#Палиндром

# s = input()
# if s[::] == s[::-1]: 
#     print('YES')
# else:
#     print('NO')

# #
# s = input()
# print(len(s), s*3, s[0], s[0:3], s[-3:], s[::-1], s[1:len(s)-1], sep='\n')
# print(s[1:][:-1])   #удаление первого и последнего символа вместо s[1:len(s)-1]/s[1:-1]

# #
# s = input()
# print(s[2], s[-2], s[:5], s[:-2], s[::2], s[1::2], s[::-1], s[::-2], sep='\n')

#
s = input()
a = len(s)
if a % 2 == 0:
    s1 = s[:a//2]
    s2 = s[a//2:]
else:
    s1 = s[:a//2 + 1]
    s2 = s[a//2 + 1:]
print(s2 + s1)

##
s = input()
# Математический фокус: (len(s) + 1) // 2 
# Для 6: (6+1)//2 = 3 (ровно половина)
# Для 5: (5+1)//2 = 3 (большая часть уходит в s1)
mid = (len(s) + 1) // 2
s1 = s[:mid]
s2 = s[mid:]
print(s2 + s1)

#
s = input() 
x = (len(s) + 1) // 2
print(s[x:]+s[:x])