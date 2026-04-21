a = int(input())
b = int(input())
n = int(input())
print(f'{a + b*(n - 1)}')

a = int(input())
print(f'{a}---{2*a}---{3*a}---{4*a}---{5*a}')
print(a, 2*a, 3*a, 4*a, 5*a, sep='---')

print()

a = int(input())

b = 0

for i in range(5):
    b += a
    if i == 4:
        print(b, end='')
    else:
        print(b, end="---")