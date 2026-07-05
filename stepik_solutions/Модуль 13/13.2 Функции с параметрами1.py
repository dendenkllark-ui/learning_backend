# Звездный треуголник через функцию с параметрами

def draw_box(height, width):    # функция принимает два параметра
    for i in range(height):
        print('*' * width)
draw_box(5, 7)
n = 3
m = 9
draw_box(n, m)

#
def print_hello(n):
    print('Hello' * n)
print_hello(3)
print_hello(5)
times = 2
print_hello(times)

# Введение второго параметра
def print_text(txt, n):
    print(txt * n)
print_text('Hello', 5)
print_text('A', 10)

def change_us(a, b):
    a = 0
    b = 0
    print(a, b)

x = 1
y = 7
print(x, y)
change_us(x, y)
print(x, y)

#
def triple(num):
    num *= 3

num = 10
triple(num)
print(num)