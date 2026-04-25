x = int(input())
if -1 < x < 17:
    print("Принадлежит")
else:
    print("Не принадлежит")

x = int(input())
if x <= -3 or x >= 7:
    print("Принадлежит")
else:
    print("Не принадлежит")

x = int(input())
if -3 < x < 7:
    print("Не принадлежит")
else:
    print("Принадлежит")

x = int(input())
if -30 < x <= -2 or 7 < x <=25:
    print("Принадлежит")
else:
    print("Не принадлежит")

n = int(input())
print('Принадлежит' if -30 < n <= -2 or 7 < n <= 25 else 'Не принадлежит')