# Локальные переменные
def print_texas():
    birds = 5000
    print('В Техасе обитает', birds, 'птиц.')

def print_california():
    birds = 9000
    print('В Калифорнии обитает', birds, 'птиц.')


# Глобальные переменные
birds = 5000   # глобальная переменная

def print_texas():
    birds = 1000  # локальная переменная
    print('В Техасе обитает', birds, 'птиц.')

def print_california():
    birds = 7000  # локальная переменная
    print('В Калифорнии обитает', birds, 'птиц.')

# Ключевое слово global
def print_texas():
    global birds
    birds = 5000
    print('В Техасе обитает', birds, 'птиц.')

def print_california():
    print('В Калифорнии обитает', birds, 'птиц.')

print_texas()
print_california()

x = 5

def add():
    global x
    x = 3
    x = x + 5
    print(x)

add()
print(x)