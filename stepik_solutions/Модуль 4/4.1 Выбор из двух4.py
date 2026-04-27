a = int(input())
if a <= 13:
    print("детство")
elif a <= 24:
    print("молодость")
elif a <= 59:
    print("зрелость")
else:
    print("старость")

a, b, c, d = int(input()), int(input()), int(input()), int(input())
x = a
if x >= b:
    x = b
if x >= c:
    x = c
if x >= d:
    x = d
print(x)

a, b, c, d = int(input()), int(input()), int(input()), int(input())
print(min(a, b, c, d))

a, b, c, d = int(input()), int(input()), int(input()), int(input())
num = [a, b, c, d]
print(min(num))