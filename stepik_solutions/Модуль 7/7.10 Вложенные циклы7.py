
# #Численный треугольник 3 🌶️
# n = int(input())
# for i in range(1, n + 1):
#     for j in range (1, i):
#         print(j, end='')
#     for j in range(i, 0, -1):
#         print(j, end='')
#     print()
# #
# n = int(input())
# for i in range(1, n + 1):
#     # Генерируем число из единиц: 1, 11, 111...
#     ones = (10**i - 1) // 9
#     print(ones**2)

# #Красивое время ✨
# n = int(input())
# for h in range(24):
#     for m in range(60):
#             if h**n == m:
#                 print(f'{h:02d}:{m:02d}')
# #
# n = int(input())
# for h in range(24):
#     m = h**n
#     if m < 60:
#         print(f'{h:02d}:{m:02d}')
#     else:
#         break # Если h**n стало больше 60, то для следующих h оно будет еще больше

#Цифровой корень 🌶️
n = int(input())
while n > 9:
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    n = s
print(n)

        
