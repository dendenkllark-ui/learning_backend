

#Заменить в строке код на буквы

a = input()
while '[u-' in a:
    x = a.find('[u-')
    y= a.find(']')
    code = int(a[x+3:y])
    target = a[x:y+1]
    a = a.replace(target, chr(code))
print(a)

#
n = input()
for i in range(0,len(n)):
    if n[i] == "[":
        n = n.replace(n[i:i + 8],chr(int(n[i + 3:i + 7])))
    if n.count("[") == 0:
        break
print(n)

#
n = input()
while "u-" in n:
    i = n.find("u")
    n = n.replace(n[i-1:i+7], chr(int(n[i+2:i+6])))
print(n)    


#
text = input()
for code in range(1040, 1104):
    text = text.replace(f'[u-{code}]', chr(code))
print(text)

# Шифр Цезаря

n = int(input())
a = input()
for i in a:
    i = chr((ord(i) - ord('a') - n) % 26 + ord('a'))
    print(i, end ='')

##
n = int(input())
text = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i in text:
    # ищем индекс текущей буквы в строке алфавита
    index = alphabet.index(i)
    # находим новую букву
    new_i = alphabet[index - n]
    
    print(new_i, end='')
