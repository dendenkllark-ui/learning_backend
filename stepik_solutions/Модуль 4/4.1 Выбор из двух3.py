n = int(input())
a = n // 1000
b = n // 100 % 10
c = n // 10 % 10
d = n % 10
if a + d == b - c:
    print("ДА")
else:
    print("НЕТ")

a = int(input())
b = int(input())
c = int(input())
sum = 0
if a >= 0:
    sum = sum + a
if b >= 0:
    sum = sum + b
if c >= 0:
    sum = sum + c
print(sum)

a, b, c = int(input()), int(input()), int(input())
print((a if a>0 else 0) + (b if b>0 else 0) + (c if c>0 else 0))

a, b, c, s = int(input()), int(input()), int(input()), 0
if a > 0:
    s += a
if b > 0:
    s += b
if c > 0:
    s += c
print(s)

a, b, c = int(input()), int(input()), int(input())
if c < 0:
    c = 0
if b < 0:
    b = 0
if a < 0:
    a = 0
print(a + b + c)