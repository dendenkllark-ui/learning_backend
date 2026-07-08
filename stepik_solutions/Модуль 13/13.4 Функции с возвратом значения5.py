
# Принять список чисел и вывести неповторяющийся


def eval(s):
    raw_list = [int(i) for i in s.strip("[]").split(",")]
    unique_list = []
    for x in raw_list:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list

num = eval(input())
print((num))

# Через set

def evil(s):
    return (set([int(i) for i in s.strip('[]').split(',')]))
num = evil(input())
print(num)


def get_unique(numbers):
    res = []
    for num in numbers:
        if num not in res:
            res.append(num)
    return res
numbers = eval(input())
print(get_unique(numbers))

