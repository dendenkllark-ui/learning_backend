def countdown(i):
    print(i)
    if i <= 1:
        return
    else:
        countdown(i-1)
countdown(3)
print("\n" + "="*30 + "\n")
def countdown_while(i):
    while i > 0:       # Пока число больше нуля...
        print(i)       # ...печатаем его...
        i = i - 1      # ...и уменьшаем на единицу.
    
    print("Поехали!")  # Это сработает, когда цикл закончится
countdown_while(3)